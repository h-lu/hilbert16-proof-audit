# Initial publication checks — 2 November 2026

This is a document and reproducibility check, separate from the [mathematical cross-review](2026-11-02-mathematical-cross-review.md). It is not a certificate of the Hilbert bound.

| Check | Observed result |
| --- | --- |
| Pinned upstream source retrieval | All 16 manifest files downloaded from the specified Git commit and matched their SHA-256 digests. |
| Claim ledger | 14 claim IDs with valid source anchors, allowed statuses and an acyclic dependency graph. |
| Local document references | Local Markdown file links and all LaTeX label references resolved. External URLs and Markdown heading fragments are outside the automated check. |
| PDF build | Three `pdflatex` passes completed; 12 pages; final log has no LaTeX warnings or overfull/underfull boxes. |
| Reading inspection | Title/contents, scope page, square-system induction and final source-comparison/bibliography pages inspected as rendered images. The contents overflow was corrected before publication. |
| Documentation synchronization | README commands, package requirements, guide notation, source IDs, ledger statuses and contribution instructions checked against the files being published. |
| Public-file review | Generated caches, local environment details and credentials excluded; only the intended research documents, reading PDF and helper scripts are staged. |

Commands used from the project root:

```sh
python3 tools/fetch_sources.py
python3 tools/show_source.py counting 64 76
make check
make pdf
git diff --check
```

Hashes of the reading artifacts at publication:

- `manuscript/uniformity.tex`: `ae7dc8b55d6da6cec2c3b5c802f8f91d6db10704f8366e12632a8dac6f937daf`
- `manuscript/uniformity.pdf`: `2c04e2b4abe7dcc87ae29ecaa43905ba9bb2109899c6f094828f2d9fcf918aef`

The PDF hash identifies this reading copy. Rebuilding may change PDF metadata and bytes; byte-for-byte PDF reproducibility is not claimed. The upstream source hashes are fixed independently of local build metadata.

Remaining mathematical work is recorded in [the retestability audit](../notes/04-retestability-audit.md) and [claim ledger](claims.json). None of the document checks establishes those estimates.
