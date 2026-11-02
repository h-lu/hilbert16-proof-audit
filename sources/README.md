# Source provenance

The mathematical audit is pinned to `openai/math` commit `4eaee87548250b2682affda7d05d947c05554bae`. [manifest.json](manifest.json) records exact paths, byte counts, line counts where applicable, and SHA-256 digests. The digests were generated from Git objects at that commit, not from an unversioned web rendering.

```sh
python3 tools/fetch_sources.py
python3 tools/show_source.py counting 22 76
python3 tools/show_source.py elimination 1038 1083
```

Run these commands from the repository root. Cached files are named by source ID under `.cache/upstream/`; they are not republished in this repository. Their original license and attribution remain in force. The committed PDF under `manuscript/` is this project's own reconstruction, not the OpenAI manuscript.

| ID | Source use |
| --- | --- |
| `introduction` | Target theorem and source proof architecture |
| `flags` | Scale hierarchies and preserved free inputs |
| `separation` | Complex packet separation |
| `calculus` | Differential and implicit closure |
| `elimination` | Exact-hit induction, retestability and absolute-zero theorem |
| `additive`, `regular`, `mixed` | Primitive passage estimates |
| `subdivision` | Finite geometric templates |
| `terminal` | Terminal passage identities, ambient extensions and boundary corners |
| `counting` | Admissible domains, projection theorem, matching and final assembly |
| `main`, `macros`, `references` | Original build structure and bibliography |
| `lean-scope` | Boundary between the quintic formalization and general claim |
| `paper` | Original 160-page PDF for source theorem numbering |

The external pages and subsequent papers have their own version/access records in [the community-source note](../notes/06-community-sources.md). A link to an unversioned public discussion is a reading lead, not an immutable mathematical source. Neither a webpage's collection date nor its footer date is treated as a peer-review date.
