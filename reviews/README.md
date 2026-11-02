# Review protocol

The ledger records the **extent of work performed**, not a binary judgment that a source theorem is true or false.

| Status | Meaning |
| --- | --- |
| `reconstructed-conditional` | A detailed proof is written here, with explicit input assumptions. AI review has not found a gap in that implication. No independent human verification is claimed. |
| `mechanism-checked` | Specific local algebraic or geometric steps have been unpacked. The source's global construction or analytic estimates have not all been verified. |
| `source-obligation` | The claim is required by the source proof and identified precisely, but is not independently established here. |
| `conditional-assembly` | The target follows if all listed upstream inputs are valid. |

These are the only statuses in the initial [claim ledger](claims.json). A human review should be added as a dated, signed review record with its exact scope and repository commit. A formal check must identify the actual theorem statement, toolchain, axioms, commands, and logs; checking a different theorem in the same source family does not qualify.

## Requirements for a mathematical review record

Record the claim ID, source commit and line/statement, the precise implication checked, accepted dependencies, and method. Distinguish a missing explanation from a false assertion. For a counterexample, verify every hypothesis; an example that violates a hypothesis may illustrate its necessity but does not refute the theorem.

When a proof is repaired, retain the old finding and link the resolution. Do not silently change `source-obligation` to a stronger status because another explanatory article repeats the claim.

## Initial review scope

The [dated mathematical cross-review](2026-11-02-mathematical-cross-review.md) records the detailed scope and findings for UNI. The [initial publication checks](2026-11-02-publication-checks.md) record reproducibility checks separately.

The initial research session used parallel AI reviews of (i) the abstract counting theorem, (ii) its domain and closure hypotheses, and (iii) the matching-to-closure bridge. Agreement between these runs is useful for drafting but is not independent peer review. No reviewer identity or affiliation is attributed to a human who has not supplied a review.

The new proof of UNI avoids the source's Fubini and exceptional-parameter steps. This is a simplification of presentation. Neither those source steps nor the replacement argument has been identified here as a flaw in the general proof. The remaining principal uncertainty lies in the analytic inputs of CLOS.
