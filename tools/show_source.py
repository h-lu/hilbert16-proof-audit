#!/usr/bin/env python3
"""Print a hash-verified source excerpt with stable line numbers."""

import argparse
import sys
from fetch_sources import manifest, verified_bytes


def main():
    data = manifest()
    entries = {e['id']: e for e in data['files']}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', choices=sorted(entries))
    parser.add_argument('start', type=int)
    parser.add_argument('end', nargs='?', type=int)
    args = parser.parse_args()
    entry = entries[args.source]
    if entry['path'].endswith('.pdf'):
        parser.error('The PDF is binary; choose a TeX or Markdown source ID.')
    try:
        lines = verified_bytes(entry).decode('utf-8').splitlines()
    except FileNotFoundError:
        parser.error(f'First run: python3 tools/fetch_sources.py --only {args.source}')
    end = args.end if args.end is not None else args.start
    if not 1 <= args.start <= end <= len(lines):
        parser.error(f'Line range must satisfy 1 <= start <= end <= {len(lines)}.')
    print(f"https://github.com/openai/math/blob/{data['commit']}/{entry['path']}#L{args.start}")
    for index in range(args.start - 1, end):
        print(f'{index + 1:5}: {lines[index]}')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
