# Contributing a checkable mathematical argument

The goal is to reduce the work needed for a specialist to decide whether each implication is valid. English mathematical notes are preferred for international review; Chinese explanations and corrections are welcome.

## Report a precise issue

1. Identify the claim ID in [the ledger](reviews/claims.json) and the pinned source statement or lines.
2. State the hypotheses actually available at that point.
3. State the conclusion used by the next step.
4. Give a proof, a counterexample satisfying **all** hypotheses, or the exact missing estimate/quantifier.
5. Specify whether you checked the upstream dependencies or assumed them.

Use the issue template for a mathematical question or finding. Public discussion is welcome; do not describe an unresolved question as a confirmed gap.

## Write proofs for review

- Put the theorem statement before motivation and proof.
- Define every nonstandard class and domain condition before using it.
- Display the order of quantifiers and the dependencies of constants.
- Keep all graph ties and strict domain restrictions when changing variables or clearing denominators.
- Separate independent-variable differentiation from differentiation after substitution.
- For a sequence argument, say what was fixed before the sequence and what is allowed to depend on a subsequence.
- Give a low-dimensional example and, where useful, a counterexample to a weakened hypothesis.
- Use source links pinned to a commit, and identify any strengthened or altered statement.
- Mark unverified analytic inputs explicitly. Do not import a conclusion from an exposition as though it were a proved lemma.

## Reproduce and review changes

```sh
python3 tools/fetch_sources.py
make check
make pdf
```

Review the rendered PDF, not only TeX compilation. If the mathematical proof changes, update its guide and the ledger. Generated `.cache` files and TeX auxiliary files should stay untracked. The reading PDF is tracked so readers do not need a TeX installation.

Automated checks cover document consistency and source integrity. They do not validate arbitrary mathematical deductions.

## Attribution

Identify AI-assisted writing or review when used, and distinguish it from human review or formal verification. Cite source arguments even when reorganizing them. Contributions are submitted under the repository's Apache-2.0 license. Do not imply endorsement by OpenAI or the authors of linked community resources.
