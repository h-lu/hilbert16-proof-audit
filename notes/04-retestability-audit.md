# The analytic obligation: from a zero chart to another actual zero

中文提示：这里审查的是一般上界证明尚未独立认证的核心接口。已明确量词和必须交付的估计，但没有把“待核查”写成“已发现漏洞”。最优先的任务是：先证明精度提高不会同时毁掉逆映射邻域，再证明扰动后保留的是整个普通解析系数芽，而不只是极限处的数值。

## 1. The implication that needs an actual proof

Fix **one** finite generated equation system $\mathscr S$. Its coefficients, former parameters, graph variables and multipliers are all coordinates. Suppose it has distinct isolated solutions $z_j$. After subsequences and exact regular graph changes, the source aims to reach one of two alternatives:

1. All enlarged coordinates converge, and the normalized, divisor-cleared equations extend analytically across their limit. Local finiteness of real analytic sets then excludes accumulating isolated solutions.
2. Some coordinate remains large. An admissible flag, packet library and elimination chart retain a free input $S$ recoverable from the old solution tuple. The formal data of the normalized equations vanish identically on the final chart. Retesting after an arbitrarily small legal change of $S$ must produce another **actual** zero near $z_j$.

The second alternative contradicts isolation only if the new point is distinct in the old coordinates, lies in the original strict domain, and satisfies the original equations exactly. Small residuals or a change solely in artificial auxiliary coordinates are insufficient. This is the [source absolute-zero theorem and its proof](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/05-elimination.tex#L1053).

No common radius of isolation is required. For each $j$, one can choose the perturbation inside the intersection of that point's graph-uniqueness neighborhood, chart neighborhood, strict domain and proposed isolation ball. The nontrivial requirement is that this choice remains admissible for the asymptotic argument along the perturbed sequence.

## 2. A quantified checklist for the last contradiction

Let $\widetilde z_j=(z_j,v_j)$ be the graph-enlarged anchors. Write a final local chart as $\Gamma_j(S,t)$, with the selected local branch understood. This notation summarizes the required chart properties; it does not supply them.

The following six assertions suffice:

**R1 — Exact anchors.** $\Gamma_j(S_j,t_j)=\widetilde z_j$, not merely an approximation tending to it.

**R2 — Genuine free input.** Some coordinate of $S$ can be varied locally while the necessary chart relations remain satisfied, and its value can be recovered from the coordinates before flag changes. If the old tuple stays fixed, graph uniqueness forces every added variable on the selected branch to stay fixed. Hence changing that recoverable input changes $z_j$.

**R3 — Legal small perturbations.** For any positive sequence of required neighborhood sizes, choose nonzero changes $S'_j-S_j$ small enough to stay inside those neighborhoods, preserve the selected affine relations, sectors and strict regime gaps, and retain the same limiting ordinary data. Smallness is chosen pointwise; it is not a uniform perturbation size.

**R4 — Identity of terminal germs.** After identifying the preserved flag descriptions, every terminal ordinary coefficient is the same analytic germ before and after retesting. Equality only at the limiting point, equality only on the old sequence, or agreement to finitely many formal orders does not suffice.

**R5 — Stability under the finite recipe.** The finite algebraic, differentiated, Taylor and regular implicit operations used to form the final chart act on those same germs and select the same regular root germs. Both all-zero formal arrays therefore remain zero. If a graph Jacobian degenerates at the limit, it is retained as an equation; it cannot be inverted using a theorem that assumes a nonzero limiting Jacobian.

**R6 — Exact separation.** The perturbed objects satisfy the full complex packet hypotheses of separation. All-zero formal arrays then imply actual zero values at sufficiently far perturbed anchors. Undoing nonzero normalizations and the exact graph identities gives $\mathscr S(z'_j)=0$.

R1–R6 imply a contradiction to isolation. R2 is addressed by graph recovery; R4 is the primitive retestability claim; R1 and R5 carry much of the elimination burden. The [source application](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L864) asserts these interfaces together. This note separates them so they can be checked independently.

## 3. The quantifier order in exact-hit correction

Source Proposition 5.5 proves exact, visible and negligible alternatives simultaneously. The negligible alternative is not just an approximation statement. For fixed field tolerance $M$, an eventual floor realization $r\to0$, and finite derivative request $k$, the required order is schematically

$$
\forall(M,r,k)\quad \exists\text{ structural list and power exponents}\quad
\forall\mathcal A\quad \exists C_{\mathcal A},j_{\mathcal A},\text{ finite replay recipe}.
$$

The power exponents controlling forward maps, record outputs, inverse Jacobians, and source and image neighborhoods are fixed **before** requesting record accuracy $\mathcal A$. Constants, Taylor depths and the starting index may depend on $\mathcal A$. Completed charts stay fixed. See the [precise proposition](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/05-elimination.tex#L618) and [common-domain lemma](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/05-elimination.tex#L403).

A simple estimate shows why this order matters. Suppose an approximate image misses its target by $O(r^{\mathcal A})$, an inverse costs $O(r^{-C})$, and an available source radius is $c_{\mathcal A}r^N$, where $C,N$ are fixed. An inverse correction costs $O(r^{\mathcal A-C})$. Choosing $\mathcal A>C+N$ puts that correction inside the source radius for sufficiently small $r$. A fixed image exponent can be handled in the same choice. Constants depending on $\mathcal A$ cause no problem because $\mathcal A$ has already been fixed before taking $j\to\infty$.

In contrast, an error $r^{\mathcal A}$ need not fit inside a radius $r^{2\mathcal A}$ for any accuracy: their ratio is $r^{-\mathcal A}\to\infty$. Merely proving an inverse function theorem separately for each replay depth is therefore insufficient. This is a diagnostic example, **not** a counterexample to the source, which explicitly claims the stronger order.

To certify R1, a reviewer should trace the exponents through every induction prefix, including record derivatives and the Schur complement in a lifted thickness equation. A bound on the final flattened formula alone does not establish a fixed image radius.

## 4. Why coefficient germs and current backgrounds matter

### Values at the limiting point do not determine germs

The analytic germs $a(t)=t$ and $b(t)=0$ agree at $t=0$ but are different. If a later ordinary restriction changes $t$, they give different formal coefficients. Retestability must preserve the germ as a function of the ordinary variables. This is exactly stronger than retaining a limiting numerical coefficient.

### Flatness does not establish equality

For every fixed $A>0$, $e^{-S^2}=o(e^{-AS})$ as $S\to\infty$, yet the function is nonzero. Thus agreement to all fixed exponential orders on the real axis does not prove that a discarded remainder is zero. The source must retain the lateral/Stokes data and prove the full domain and growth assumptions of its separation theorem. This example tests a weakened premise, not the actual complex packet class.

### Tiny ordinary changes can change a large scale substantially

Take $Q(S,x)=\exp(\exp(S+x))$ and $x=e^{-S-B}$, with fixed bounded $B$. Then

$$
\log\frac{Q(S,e^{-S-B})}{Q(S,0)}
=e^S\bigl(e^{e^{-S-B}}-1\bigr)\longrightarrow e^{-B}.
$$

Replacing the current background by its limiting value $x=0$ loses a nontrivial multiplicative effect. The source explicitly evaluates monomials at current backgrounds. A review must check that this convention survives every Taylor replay and inverse estimate; it cannot be justified merely by $x\to0$.

### Tied derivatives are not independent derivatives

The expression $E(u,v)=u-v$ vanishes on the graph $u=v$, but $\partial_uE=1$ as an independent derivative. A correct formula only on the physical endpoint graph cannot by itself control the independent derivatives needed by multiplier systems. Exact ambient identities and their retained graph equations must supply the missing information. See [the closure contracts](03-closure-contracts.md).

## 5. What the primitive sections claim to deliver

The following are **source proof obligations**, not new assertions established by this audit. Each row says where a specialist can begin checking R4–R6.

| Primitive | Claimed canonical data after extraction | What must be checked |
| --- | --- | --- |
| Additive passages | Triangular charge recursions and fixed primitive constants; surviving inner kernels have normalized infinite-anchor jets | Compatibility of finite budgets; uniqueness and parameter/derivative dependence of the normalized jets; no lost lateral contribution when a cutoff is retired |
| One-rate regular/stable passages | Imbalance division, balanced projection, graph and fiber recursions at fixed formal degree | Numerical large inputs and integration anchors never enter terminal initial data; cutoff retirement preserves every fixed coefficient germ |
| Two-scale mixed passages | Comparable regime: exact residues and analytic cluster integrals; small slope: fixed residue products; fast damping: compatible graph/fiber recursions | Regime changes and charge collisions preserve the same germs, including independent derivatives and controlled input tests |

Pinned starting points: [additive retesting](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/06-additive.tex#L1713), [regular retesting](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/07-regular.tex#L643), [mixed retesting](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/08-mixed.tex#L1381).

For each fixed formal label, derive an identity of ordinary analytic germs from a specified recursion or normalization. Then verify that the identities apply to every label in the support. One need not invent a common finite truncation for an infinite array; one must prove the rule defining each coefficient is invariant. Conversely, checking a few leading coefficients does not establish R4.

The scope must include every **fixed finite derivative request** generated from a fixed system. The theorem does not demand one constant or one complex neighborhood for all derivative orders. It does demand the prescribed uniformity within each controlled family for that fixed request. Confusing these two requirements can create either a false objection or an insufficient proof.

## 6. Boundary coverage is a separate obligation

Positive-margin completeness controls bounded limits only when every listed margin stays bounded away from zero. It says nothing at a vanishing margin. The absolute-zero proof must handle those limits separately.

The [boundary-corners lemma](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/10-terminal.tex#L948) claims a dichotomy after finite graph additions: either an enlarged coordinate diverges, or all normalized kernel factors have analytic extensions with state room at their bounded limits. Cleared graph equations may be singular at the limit; local uniqueness is required at the selected sequence points.

This is stronger than the domain hypothesis of the projection theorem. A complete audit should enumerate working-box boundaries, structural divisors, zero clock lengths, vanishing rates and unbounded auxiliary ratios. If only a multiplier or auxiliary ratio diverges while kernel clocks remain bounded, the bounded kernel should be treated by ordinary analytic dependence, not by a two-large-clock theorem whose hypotheses fail.

## 7. Review tasks with completion criteria

| Task | Concrete deliverable | What does not count as completion |
| --- | --- | --- |
| A1: exact-hit correction | A table of each induction prefix's forward, record, inverse, source and image exponents, showing independence from later $\mathcal A$ | Saying that each finite recipe is analytic or locally invertible |
| A2: old free input | A dimension and recovery argument through every promotion, restriction and graph addition, identifying an input whose change alters the old tuple | Exhibiting an arbitrary newly added free variable |
| A3: additive retest | Derive one complete coefficient recursion, its normalization and budget compatibility, then generalize with all derivative/domain estimates | Equality of values only at the limiting ordinary point |
| A4: regular/mixed retest | Check each slope regime and cutoff-retirement rule as identities of terminal germs | Dropping a remainder because it is flat on the real axis |
| A5: full generated closure | Start with an arbitrary fixed finite list of independent derivatives and multipliers, and verify that the same sequential dichotomy and R1–R6 apply | Checking only the original transfer equation |
| A6: boundary corners | Enumerate every strict margin and prove analytic extension or divergent-coordinate reduction for its vanishing limits | Reusing positive-margin completeness at a zero margin |
| A7: geometric termination | Check the order-decreasing box induction and the claimed one-time resonance redo, with all degeneracies retained | A finite subdivision constructed after choosing a bad sequence |

A useful first submission would complete A1 for a single nontrivial negligible-center lift, with all constants and dependency arrows displayed. The next submission can verify a primitive coefficient recurrence through that same lift. This tests the hardest interface on an explicit instance before attempting the entire construction.

## 8. Present conclusion

The source explicitly states the strong requirements above. Their presence rules out several superficial gap claims; stating them is not the same as proving them. This audit has established the downstream conditional projection implication and unpacked the final contradiction, but has not independently certified the complex estimates and exact-hit induction that deliver R1–R6 for every generated matching system. No concrete counterexample satisfying all of the source's hypotheses has been established here.
