# Community sources and their evidential limits

**中文导读。** 两处用户提供的页面都已重新读取。社区索引目前标注更新至 2026-10-30，并新增一篇 10 月 23 日的 Rayleigh–Liénard 论文；已回到该论文原文，确认它把 OpenAI 的一般上界称为需要独立核查的预印本主张。Latent Seminar 提供有用的论证提纲，但明确不声称完整独立验证。本审计采用它们提供的检索线索和问题区分，证明判断以固定版本的原文和本仓库的逐步论证为准。

Access date for the sources below: **2026-11-02**. Dates in the provenance table are the dates displayed by the sources, not inferred dates of their last substantive mathematical revision. Manuscript audit target: `openai/math` commit `4eaee87548250b2682affda7d05d947c05554bae`.

## 1. The two supplied pages

| Source | Dated provenance observed | Useful contribution | Limit and treatment in this audit |
|---|---|---|---|
| [Math Community: Uniform bounds for planar polynomial limit cycles](https://mathcommunity.github.io/oai-math-revised/papers/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/) | Page footer: updated 2026-10-30. Its automatically collected material also bears 2026-10-30 and identifies the tools used. The human-contribution notes area is empty. | Leads to primary follow-up literature; separates the arbitrary-degree claim from the quintic Lean result; links a public Comparator log. | The page explicitly labels the collected material unreviewed. We follow its links and verify the relevant primary passages; an index entry, citation or absence of comments is not a verdict on the proof. |
| [Latent Seminar: Polynomial limit cycles](https://lowrank.github.io/latent-seminar/OpenAI-Math/143-polynomial-limit-cycles) | Displayed article date: 2026-10-06; no separate last-modified date observed. Its general-manuscript link pins the original `adc7f124` release. | Distinguishes individual finiteness from parameter-uniform finiteness; highlights finite templates, differential closure, the common-sign rotation count and finite-selection scaling. | It expressly limits its coverage to statements, introductions and selected mechanisms. Its summary is a reading guide, not independent verification. We reconstruct the geometric argument in [05-geometric-reductions.md](05-geometric-reductions.md), retaining the upstream hypotheses. |

Version check: the full `build/sections/11-counting.tex` fetched at `adc7f1241b42e322a6451854ab7e4b4c146bf78a` and at the audit target has the same 53,721 bytes and SHA-256 `9117c4eb330a50c7125b5c92dc53cbb227b87ef390188c6992d064bec828b20f`. This verifies the relevant section's identity across those two commits; it is not a check of every file in either release.

## 2. Primary follow-up sources checked

### Chen–Xiao–Zhang: a citation accompanied by a verification reservation

Hebai Chen, Dongmei Xiao and Rui Zhang, *Some new criteria for the uniqueness of limit cycles in Rayleigh–Liénard systems*, [arXiv:2610.33114v1](https://arxiv.org/abs/2610.33114v1), submitted 2026-10-23. The [versioned primary text](https://arxiv.org/html/2610.33114v1) cites OpenAI in its introduction and says the uniform-boundedness arguments “call for careful independent verification.” Its bibliography identifies the uniform-limit-cycle preprint.

The paper establishes its own uniqueness criteria under hypotheses on Rayleigh–Liénard damping and restoring terms. This citation records awareness and a reservation; it is neither a confirmation nor a specific counterexample to OpenAI's general proof. We adopt that limited bibliographic fact. We do not use its specialized uniqueness theorems to repair the general counting argument, and we have not independently audited its proofs.

### Qin–Sun: complementary lower bounds, explicitly independent

Chaoyang Qin and Xiaoming Sun, *Hierarchical Melnikov Realization: Logarithmic Factor Improvement to Hilbert Number Lower Bounds*, [arXiv:2610.12218v1](https://arxiv.org/html/2610.12218v1), dated 2026-10-08. The primary abstract and Theorem 1.1 state a construction yielding $H(d)=\Omega(d^2\log^2d)$. Its concluding remark says the main results were obtained by the end of August and are independent of the October 6 OpenAI release. Its disclosure identifies substantial AI assistance.

We adopt the direction of the claimed result and the authors' independence statement as provenance. A growing lower bound is compatible with a finite but noneffective upper bound at each fixed degree. This work therefore does not validate or contradict the claimed uniform upper bound. Its separate Lean-certification claim is outside this audit and was not reproduced here.

### Gasull–Santana: earlier context for hyperbolic realization

Armengol Gasull and Paulo Santana, *A note on Hilbert 16th Problem*, [arXiv:2407.13465v2](https://arxiv.org/abs/2407.13465v2), revised 2024-10-01; [published version](https://doi.org/10.1090/proc/17116). The abstract discusses realization of a finite Hilbert number by structurally stable fields with hyperbolic cycles.

This provides prior context for the final reduction, not an independent verification of the 2026 manuscript. Our argument uses arbitrary finite selections and proves the needed perturbation statement directly. It does not assume that a global finite Hilbert number is already known or attained. No novelty assessment is made here.

## 3. Formalization scope and what an accepted log actually concerns

The [pinned OpenAI scope note](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/143.md) covers only

$$
\dot x=y-F(x),\qquad \dot y=-x,\qquad \deg F\le5:
\quad\#\{\text{limit cycles}\}\le2,
$$

with equality for some $F$. It does not list a formalization of arbitrary-degree planar polynomial uniform boundedness.

The community page links the [QuinticLienard Comparator log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/QuinticLienard.log). Its final output records acceptance of `OAI.Analysis.LienardCycles.Main`. The [run documentation](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md) dates the batch to 2026-10-25–26, describes the checked revision and discloses prior compilation in the same workspace. We checked the published record; we did not rerun it. It supports a machine-check claim about the quintic statement, not the general theorem audited here.

## 4. Adoption record

| Item | Adopted | Not inferred |
|---|---|---|
| Community bibliography | Primary-source leads, authors, version dates and the verified citation context above. | Expert acceptance, a repaired proof, or exhaustive coverage of public discussion. |
| Latent Seminar's outline | A list of interfaces worth checking; the distinction between finite geometric templates and sequence-dependent auxiliary subdivisions. | That those interfaces have been proved merely because the outline describes them. |
| Signed-rotation explanation | Recomputed determinant variation, root parity and finite common-sign counting, with explicit quantifiers in note 05. | Persistence of every original cycle for the chosen sign. |
| Spatial scaling | A finite-selection reduction after an all-coefficient hyperbolic bound on a fixed square. | Prior finiteness of all cycles, or uniform coefficient compactness. |
| Family-level Lean links | Evidence of a separate quintic theorem and the scope boundary. | A formal proof of the arbitrary-degree Hilbert bound. |

The primary new bibliographic finding is the October 23 Rayleigh–Liénard article's explicit verification reservation. None of these sources changes the mathematical obligation to establish the full closure and completeness hypotheses for the general manuscript's matching systems.
