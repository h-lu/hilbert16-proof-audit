#!/usr/bin/env python3
"""Check source integrity and document wiring, not mathematical correctness."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from fetch_sources import ROOT, manifest, cache_path, verified_bytes

STATUSES = {'reconstructed-conditional', 'mechanism-checked',
            'source-obligation', 'conditional-assembly'}


def check():
    data = manifest()
    entries = {entry['id']: entry for entry in data['files']}
    cached = 0
    for entry in entries.values():
        if cache_path(entry).exists():
            verified_bytes(entry)
            cached += 1
    print(f'PASS source manifest: {len(entries)} entries, {cached} cached hashes checked')

    ledger = json.loads((ROOT / 'reviews' / 'claims.json').read_text())
    assert ledger['source_commit'] == data['commit'], 'Ledger/source commit mismatch'
    claims = {claim['id']: claim for claim in ledger['claims']}
    assert len(claims) == len(ledger['claims']), 'Duplicate claim ID'
    for claim in claims.values():
        assert claim['status'] in STATUSES, f"Unknown status: {claim['id']}"
        assert claim['depends_on'] is not None
        for dependency in claim['depends_on']:
            assert dependency in claims, f"Unknown dependency: {dependency}"
        for note in claim['notes']:
            assert (ROOT / note).is_file(), f'Missing review note: {note}'
        for source in claim['sources']:
            entry = entries[source['id']]
            assert 1 <= source['line'] <= entry['lines'], f"Invalid source anchor: {claim['id']}"
    completed = set()

    def visit(identifier, active):
        assert identifier not in active, f'Dependency cycle involving {identifier}'
        if identifier in completed:
            return
        for dependency in claims[identifier]['depends_on']:
            visit(dependency, active | {identifier})
        completed.add(identifier)

    for identifier in claims:
        visit(identifier, set())
    print(f'PASS claim ledger: {len(claims)} claims, source anchors and acyclic dependencies')

    links = 0
    for path in ROOT.rglob('*.md'):
        if any(part.startswith('.') for part in path.relative_to(ROOT).parts):
            continue
        content = path.read_text()
        content = re.sub(r'```.*?```', '', content, flags=re.S)
        for match in re.finditer(r'\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', content):
            target = match.group(1).strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            assert destination.is_relative_to(ROOT), f'Link leaves repository: {path}: {target}'
            assert destination.exists(), f'Missing local link: {path}: {target}'
            links += 1
    print(f'PASS local Markdown file links: {links} (section fragments and external URLs not checked)')

    tex_path = ROOT / 'manuscript' / 'uniformity.tex'
    tex = tex_path.read_text()
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    assert len(set(labels)) == len(labels), 'Duplicate LaTeX labels'
    for reference in re.findall(r'\\(?:eqref|ref|autoref)\{([^}]+)\}', tex):
        assert reference in labels, f'Undefined LaTeX reference: {reference}'
    print(f'PASS LaTeX label references: {len(labels)} labels')
    print('Document checks passed. These checks do not verify the mathematical proof.')


if __name__ == '__main__':
    try:
        check()
    except (AssertionError, OSError, ValueError, KeyError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
