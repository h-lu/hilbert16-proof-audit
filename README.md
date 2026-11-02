# Hilbert 16: a proof audit and reconstruction

[中文导读](README.zh-CN.md) · [Read the uniformity paper (PDF)](manuscript/uniformity.pdf) · [Proof map](notes/00-proof-map.md) · [Review ledger](reviews/claims.json)

This is a public research notebook for making OpenAI's proposed general bound for planar polynomial limit cycles easier to understand and independently check. It reconstructs arguments, states the exact interfaces between them, and records what still needs verification.

**Current result:** a self-contained reconstruction of the *conditional* projection theorem (source Theorem 11.2). Under its full differential–algebraic closure and domain hypotheses, absolute isolated-zero finiteness implies a uniform bound on fiber components. The application of these hypotheses to the passage systems remains under investigation. This repository does **not** certify the general Hilbert bound, and does not contain a Lean proof of it.

The source manuscript is [Uniform bounds for planar polynomial limit cycles](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf), dated September 24, 2026. All mathematical source references are pinned to commit `4eaee87548250b2682affda7d05d947c05554bae`. Research snapshot: **November 2, 2026**.

## Where to start

| Your question | Read |
| --- | --- |
| What exactly is claimed, and what must be checked? | [Proof map and conditional assembly](notes/00-proof-map.md) |
| What do the unusual terms mean? | [中文入门与术语表](notes/01-reading-guide.zh-CN.md) |
| Why does absolute finiteness give a parameter-uniform bound? | [Complete English proof](manuscript/uniformity.pdf), [LaTeX source](manuscript/uniformity.tex), [中文导读](notes/02-uniformity-guide.zh-CN.md) |
| Does the application supply the required closure? | [Closure contracts](notes/03-closure-contracts.md) |
| What is the next unresolved analytic task? | [Retestability audit](notes/04-retestability-audit.md) |
| How do hyperbolic cycles give all isolated cycles, anywhere in the plane? | [Geometric reductions](notes/05-geometric-reductions.md) |
| What do the community pages actually establish? | [Sources and verification scope](notes/06-community-sources.md) |
| How can I contribute a precise mathematical objection? | [Contribution protocol](CONTRIBUTING.md) |

The uniformity proof uses one common generic linear tilt for a **countable witness family**. This removes the source proof's Fubini step and its exceptional-parameter continuation step. It is an expository reorganization of the same critical-point method, not a claim of a new Hilbert theorem.

## What is and is not checked

| Part | Repository status |
| --- | --- |
| Abstract projection/counting implication | Full conditional proof reconstructed; AI cross-review recorded; human review invited |
| Necessity of closure and complete domain margins | Two explicit counterexamples worked out |
| Regular graph lifting, chain-rule reconstruction, parameter bookkeeping | Local mechanisms unpacked; their analytic inputs remain explicit assumptions |
| Signed rotation and spatial scaling | Proof rewritten from standard return-map arguments |
| Separation, implicit packet calculus, elimination, primitive estimates, finite preparation | Source obligations; no complete independent verification here |
| General degree-only bound | Conditional on the unresolved source obligations |
| Formal verification | None for the general bound or this reconstruction |

Status names and claim IDs are defined in [the review protocol](reviews/README.md). Passing the repository checks means that sources, references, and document builds are consistent; it is **not** a mathematical certificate.

## Reproduce the reading environment

Requirements: Python 3.10+, and a TeX installation with `pdflatex`, `amsmath`, `amsthm`, `amssymb`, `geometry`, `hyperref`, `enumitem`, `booktabs`, `array`, and `microtype` for rebuilding the PDF.

```sh
python3 tools/fetch_sources.py
python3 tools/show_source.py counting 64 76
make check
make pdf
```

`fetch_sources.py` downloads only the files listed in [sources/manifest.json](sources/manifest.json), checks their SHA-256 digests, and places them in ignored `.cache/upstream/`. It does not require a GitHub login or clone the large Lean tree. See [source provenance](sources/README.md). `show_source.py` prints immutable source locations with line numbers. `make check` verifies the source manifest, local document links, and review-ledger dependencies. `make pdf` rebuilds the committed reading copy from its LaTeX source with three passes to settle its contents and cross-references.

## Research priorities

1. Verify the exact-hit and retained-free-input assertions of source Proposition 5.5, including the order in which inverse estimates and approximation accuracy are fixed.
2. Verify that the additive, regular, and mixed primitive theorems provide the **same terminal coefficient germs** after the perturbations used in Theorem 5.7.
3. Check these statements for arbitrary fixed finite derivative requests in the full closure, not just for the original matching equations.
4. Audit the finite preparation and resonance termination behind the finite geometric alphabet, independently of sequence-dependent analytic subdivisions.

Each task has a concrete success criterion in the [audit notes](notes/04-retestability-audit.md) and [claim ledger](reviews/claims.json). An unchecked step is an open review task, not an established flaw.

## Provenance and authorship

The initial notes were prepared with Codex and parallel AI review. Multiple AI passes are not independent human peer review. No mathematician's endorsement is implied. The source's quintic Liénard formalization is a separate result; [its scope note](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/143.md) does not formalize the arbitrary-degree bound.

The two requested community resources are examined in [the source review](notes/06-community-sources.md). They are useful guides and reference indexes; neither is used as a substitute for a proof of the source's analytic estimates.

Original contributions in this repository are distributed under [Apache-2.0](LICENSE). See [NOTICE](NOTICE) for upstream attribution. Contributions should identify the exact source version, hypotheses, and verification method.

Edition changes are recorded in [CHANGELOG.md](CHANGELOG.md).
