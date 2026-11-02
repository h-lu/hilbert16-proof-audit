#!/usr/bin/env python3
"""Fetch pinned mathematical source files; verify bytes before caching them."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache' / 'upstream'


def manifest():
    data = json.loads((ROOT / 'sources' / 'manifest.json').read_text())
    if data['repository'] != 'openai/math':
        raise ValueError('The source repository must be openai/math.')
    if not re.fullmatch(r'[0-9a-f]{40}', data['commit']):
        raise ValueError('An immutable 40-digit commit is required.')
    seen = set()
    for entry in data['files']:
        path = PurePosixPath(entry['path'])
        if path.is_absolute() or '..' in path.parts or not path.parts:
            raise ValueError('Invalid relative source path.')
        if not re.fullmatch(r'[a-z0-9-]+', entry['id']) or entry['id'] in seen:
            raise ValueError('Source IDs must be unique and filename-safe.')
        seen.add(entry['id'])
        if not re.fullmatch(r'[0-9a-f]{64}', entry['sha256']):
            raise ValueError('Missing SHA-256 digest.')
    return data


def cache_path(entry):
    return CACHE / (entry['id'] + PurePosixPath(entry['path']).suffix)


def verified_bytes(entry):
    payload = cache_path(entry).read_bytes()
    if hashlib.sha256(payload).hexdigest() != entry['sha256']:
        raise ValueError(f"Hash mismatch for {entry['id']}; remove that cache file and refetch.")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only', help='Fetch just one source ID from the manifest.')
    args = parser.parse_args()
    data = manifest()
    entries = [e for e in data['files'] if not args.only or e['id'] == args.only]
    if not entries:
        parser.error(f'Unknown source ID: {args.only}')
    CACHE.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        destination = cache_path(entry)
        if destination.exists():
            verified_bytes(entry)
            print(f"verified  {entry['id']} (cached)")
            continue
        url = f"https://raw.githubusercontent.com/openai/math/{data['commit']}/{entry['path']}"
        request = urllib.request.Request(url, headers={'User-Agent': 'hilbert16-proof-audit-source-fetcher'})
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = response.read(10_000_001)
        if len(payload) > 10_000_000:
            raise ValueError(f"Source unexpectedly exceeds 10 MB: {entry['id']}")
        if hashlib.sha256(payload).hexdigest() != entry['sha256']:
            raise ValueError(f"Downloaded hash mismatch: {entry['id']}; nothing saved.")
        temporary = destination.with_suffix(destination.suffix + '.part')
        temporary.write_bytes(payload)
        temporary.replace(destination)
        print(f"verified  {entry['id']} ({len(payload)} bytes)")
    print(f'All {len(entries)} selected source files match the pinned manifest.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, urllib.error.URLError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
