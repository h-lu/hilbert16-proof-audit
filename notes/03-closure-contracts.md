# From matching equations to absolute zeros: closure contracts

中文导读：本文把“匹配系统的有限微分代数闭包”拆成可逐项验证的逻辑接口。图增广、有限阶链式法则和清分母的局部论证已独立核对；覆盖所有边界序列的 packet 估计仍是条件，不能据此宣称总证明成立。

**Audit scope.** OpenAI, *Uniform bounds for planar polynomial limit cycles*, source pinned to commit `4eaee87548250b2682affda7d05d947c05554bae`. This note identifies the contracts by which the matching systems of Theorem 11.4 could satisfy Theorem 11.2, including the conditional use of Theorem 5.7. “Checked” means that the displayed local argument has been independently reconstructed; it does not certify the primitive estimates or the complete proof. All source links below identify this fixed version.

## 1. What must actually be proved

Write the original matching data as

$$
 F(p,x)=0,\qquad (p,x)\in U,\qquad g_j(p,x)>0.
$$

Let $\mathscr C(F,g)$ consist of **finite** augmented systems generated from these data by the operations actually used in the projection proof: finite independent-coordinate differentiation, algebra, declared inverses, added real coordinates, polynomial equations, parameter specializations, and determinant restrictions. Every member retains the original equations, argument ties and open restrictions. The required statement is

$$
 \boxed{\forall S\in\mathscr C(F,g),\quad
       \#\operatorname{Iso}(Z(S))<\infty.}
 \tag{C-AZP}
$$

Here every coordinate of $S$, including former parameters and Lagrange multipliers, is an unknown. There is no bound asserted uniformly over all $S$. Theorem 5.7 is conditional: its closure clause still requires the sequential hypotheses for the particular generated system. Reading that clause as automatic closure would remove the principal obligation of Theorem 11.4. See the [absolute-zero theorem and its explicit qualification][absolute].

This distinction is substantive. For example, on $t>0,\ 0<x<1$, the equation $\sin(tx)=0$ has no isolated points in its total two-dimensional solution locus, while its fibers have unbounded finite cardinalities. The permitted extra polynomial equation $x=1/2$ produces infinitely many isolated total solutions $(2k\pi,1/2)$. Thus the original total zero set alone is insufficient. This example diagnoses a missing hypothesis; it is not an example from the paper's primitive library.

The proof under audit starts correctly by fixing one arbitrary finite $S$ and one alleged infinite sequence of isolated solutions. Its algebraic description is made hereditary under further multiplier and determinant constructions in [§11, lines 705–722][closure-start].

## 2. Contract G: exact regular graph lifting

**Inputs.** An original solution tuple $u_i$, an enlargement $(u,v)$, analytic equations $G(u,v)=0$, and a selected solution $v_i$ with

$$
 \det G_v(u_i,v_i)\ne0.
$$

**Required output.** On an open neighborhood $N_i$ of $(u_i,v_i)$, the enlarged solution set is the graph of a single analytic function $v=g_i(u)$, and projection is an analytic isomorphism onto the original solution germ.

**Independent derivation.** The implicit function theorem supplies the graph. Substitution into the remaining enlarged equations must give the original equations as actual functions on an open old-argument neighborhood, not only on their zero sets. The graph projection and its inverse $u\mapsto(u,g_i(u))$ then preserve isolated points in both directions. Neither a common radius for all $N_i$ nor a nonzero limiting determinant is required.

For a composition of $K$ flows, retain

$$
 z_j-\Phi_j(a_j(u),z_{j-1})=0,\quad 1\le j<K.
$$

The Jacobian in the intermediate states is triangular with identity diagonal. This establishes local uniqueness without invoking a global uniqueness theorem for the augmented equation set. This part of [the graph-and-jet lemma][graph-jet] is **checked**, conditional on the asserted decomposition being an exact identity of the old independent kernel.

**Failure criterion.** A purported rewrite fails this contract if it changes an off-graph independent argument, selects an auxiliary value without a locally unique graph, or needs a different number of intermediate states at every member of the selected subsequence. Equality only on the physical matching locus does not pass.

## 3. Contract D: reconstruct the requested derivatives

The derivative interface is stronger than value agreement. If

$$
 \Phi(u)=\Psi(u,v(u)),\qquad G(u,v(u))=0,
$$

then

$$
 v_{u_j}=-G_v^{-1}G_{u_j},\qquad
 \Phi_{u_j}=\Psi_{u_j}+\Psi_vv_{u_j}.
$$

At order $k$, implicit differentiation expresses each derivative of $v$ through jets of $G$ of order at most $k$, lower-order derivatives of $v$, and $G_v^{-1}$. Cramer's rule therefore gives a rational expression in finitely many analytic jets with a finite power of $\det G_v$ in the denominator. A finite stack of graphs retains this property. If derivatives are adjoined as coordinates instead of substituted, the equations for the highest-order jet are linear in that jet with coefficient $G_v$; the complete jet Jacobian is block triangular.

A concrete check is

$$
 S=Q-q,\qquad M=(Q-q)/q,
 \qquad \Phi(Q,q,\delta,\eta)=\Psi(S,M,\delta,\eta).
$$

Holding $\delta,\eta$ fixed gives exactly

$$
 \Phi_Q=\Psi_S+q^{-1}\Psi_M,
 \qquad
 \Phi_q=-\Psi_S-Qq^{-2}\Psi_M.
$$

Both formulas in [the source's reconstruction step][derivatives] pass direct differentiation. For a further check,

$$
 \Phi_{QQ}=\Psi_{SS}+2q^{-1}\Psi_{SM}+q^{-2}\Psi_{MM},\qquad
 \Phi_{qq}=\Psi_{SS}+2Qq^{-2}\Psi_{SM}+Q^2q^{-4}\Psi_{MM}+2Qq^{-3}\Psi_M.
$$

The $\Psi_M$ terms cannot be omitted. These finite algebraic claims are **checked**; the availability and estimates of all primitive jets appearing on the right remain upstream obligations.

## 4. Contract R: clear denominators without changing the domain

After finitely many permitted operations, each equation can be written

$$
 A(u,v)/B(u,v)=0
$$

on its declared domain $B\ne0$, where $A,B$ are finite algebraic combinations of the primitive and graph jets. It can be replaced by $A=0$ **with $B\ne0$ retained**. Inverting a previously constructed rational expression also adds its numerator to the nonzero restrictions. This is a finite symbolic calculation, not an estimate on $1/B$.

The distinctions that matter are:

| Operation | What is justified | What is not justified |
| --- | --- | --- |
| Clear an equation denominator | Same solution germ on its original nonzero domain | Equality of the zero sets after adding $B=0$ points |
| Preserve a strict inequality | An interior point retains an open neighborhood in that domain | An arbitrary numerator-sign replacement without tracking denominator signs |
| Let $B(u_i,v_i)\to0$ | Pointwise graph equivalence may survive | A uniform inverse bound or regularity at the limiting tuple |
| Adjoin a jet as a coordinate | A finite regular graph at each sequence point | That the new coordinate stays bounded |

This reconstructs the [cleared finite differential closure lemma][clear] without assuming a nonsingular limiting graph. It is **checked** as a local algebraic implication.

## 5. Contract B: bounded enlarged tuples

The bounded alternative must concern the **entire enlarged tuple**, not just the old physical variables. Suppose $(u_i,v_i)\to(u_*,v_*)$ and all primitive factors and defining graph equations extend analytically to one neighborhood of this finite tuple. Contract R converts the remaining equations to analytic equations on that neighborhood. Pointwise isomorphism makes every lifted selected solution isolated.

An isolated zero cannot be created at an interior point by intersecting a positive-dimensional analytic germ with an open restriction: a small neighborhood already lies in that restriction. Local finiteness of connected components of an analytic set therefore excludes the accumulating isolated sequence. No extension of the inequalities to a useful sign at the limit is needed for this argument.

This is distinct from positive-margin completeness. Completeness proves properness of the projection barrier only when margins stay bounded away from zero. It says nothing about analytic extension at a vanishing margin. The source correctly supplies a separate [boundary-corner lemma][corners] and uses it in the [bounded-tuple argument][bounded].

**Status.** The implication “analytic extension of the enlarged primitives ⇒ no accumulating isolated sequence” is checked. The extension hypothesis is not independently certified here. In particular, verifying actual state room for all independent ambient parameters requires the estimates behind the boundary-corner lemma, not just its list of cases.

## 6. Contract U: divergent enlarged tuples

If one enlarged coordinate diverges, the required deliverable is one common finite saturated flag for the finite collection of kernels and algebraic factors in the chosen system. It must supply:

1. a locally invertible real coordinate representation, including signed large coordinates and bounded remainders;
2. the requested independent jets of every old kernel, reconstructed using Contract D;
3. finite nonzero monomial normalizations and the positive operations used by elimination;
4. a common retestable primitive library after all graph equations are retained;
5. at least one surviving old free input recoverable from the enlarged tuple.

There is an important special case. A multiplier, derivative coordinate or auxiliary ratio may diverge while every primary clock of a kernel remains bounded. Then that kernel should retain its bounded-clock analytic formula and be constant in the extra free input before pullback. Divergence of the auxiliary ratio alone does not justify applying a mixed theorem whose hypotheses require both primary clocks to diverge. The source expressly handles this in [lines 838–862][divergent].

**Status.** The classification avoids the identified logical confusion. The universal packet coverage and the estimates needed after pullback are still assumptions to be discharged; see [the retestability audit](04-retestability-audit.md).

## 7. Contract F: finite subdivision and quantifier order

The legitimate order is

$$
 \forall S\in\mathscr C(F,g)\quad
 \forall\text{ alleged infinite isolated sequence }(u_i)
 \quad\exists\text{ subsequence, one finite }K,
 \text{ one finite enlargement, one finite flag}.
$$

For a bounded ratio converging to $M_*<\infty$, a finite $K$ may depend on $M_*$. Once chosen, it must work for every sufficiently far point of that subsequence and for the fixed derivative request. This creates one fixed finite lifted equation system to which the absolute-zero argument can apply. A scheme requiring $K_i\to\infty$ on the retained sequence does not satisfy this contract.

No uniform bound on $K$ across all sequences follows or is needed at this stage. The sequence-dependent subdivisions are not new words in the original geometric matching family. The [source states both restrictions explicitly][finite-k].

The later projection theorem uses (C-AZP) for its finitely many generated critical-point systems. It does not require a common isolated-zero count across their infinitely many possible numerical constants. This is why finite $K$ after choosing the contradiction sequence is consistent with a parameter-uniform bound later.

## 8. Contract I: recover a change of an original solution

Let $C_i$ be the final real chart around an exact lifted hit and let $s$ be a retained free input. A useful explicit certificate is a local recovery function $R_i$ satisfying

$$
 R_i(C_i(s,t))=s.
 \tag{recover}
$$

If a nearby chart point is a solution and its original full tuple $u$ is unchanged, graph uniqueness gives $v'=g_i(u_i)=v_i$. Then (recover) forces $s'=s_i$. Consequently any nonzero permitted change of $s$ giving a nearby lifted solution changes the original tuple.

For each proposed original isolation neighborhood $B_i$, take the chart neighborhood inside both the selected graph neighborhood and $\pi^{-1}(B_i)$, and inside every strict domain. Continuity permits a separately chosen small variation. A determinant tending to zero affects the permitted radius; it does not invalidate this implication. This independently reconstructs [the recovery lemma][recovery]. It does **not** prove that the varied point remains a solution—that is exactly the retestability/separation obligation.

## 9. Contract P: fixed parameters, full rank, and component injection

The geometric representation has three additional obligations before the projection count can be applied. First, for each fixed degree there must be **finitely many fixed words**, with one parameter tuple $p_w(V)$ for a field and word, independent of the selected orbit. Endpoint-dependent normalizations belong among the unknowns, with graph equations. Otherwise different cycles could be counted in different parameter fibers, and a bound on each fiber would not bound their total. This is the [explicit parameter convention][parameters]; its realization depends on the finite-template construction.

Second, a hyperbolic target gives a regular point of the fiber. Assume that, after eliminating the regular auxiliary graph, every scalar transfer is an actual local endpoint mismatch times a nonzero analytic factor. The identity is needed on an open neighborhood of proposed endpoints, including mismatched pairs. In particular, if $H(e_-,e_+,a)=U(e_-,e_+,a)\Delta_0$, substituting the endpoint-dependent normalization $a(e_-,e_+)$ gives $dH=U\,d\Delta_0$ at $\Delta_0=0$. Agreement merely at matching pairs would not justify this differential.

In flow coordinates $(s_j,r_j)$, the reduced link differentials, up to nonzero row factors, are

$$
 dr_{j+1}-h_j\,dr_j,\qquad j\in\mathbb Z/k\mathbb Z.
$$

Their kernel satisfies $dr_1=(\prod_jh_j)dr_1$. Since the product is the return multiplier and hyperbolicity makes it different from one, all transverse increments vanish. Thus these $k$ rows have rank $k$; the auxiliary graph adds an invertible block. The fiber dimension is $k$, accounting for freely movable tangential cuts. Hyperbolicity does **not** make a representation an isolated point. This [rank argument][rank] is checked conditional on the ambient mismatch identities.

Third, each connected component of a regular fiber chart must represent at most one hyperbolic orbit. Fix a nonzero maximal-minor chart and a connected component $M$. The first-endpoint map $E:M\to\mathbb R^2$ is analytic. Near a target on a hyperbolic orbit $C$, local physical validity and the unique nearby Poincaré fixed point imply $E\in C$. Since $C$ is a compact embedded regular analytic curve, set $A=\operatorname{int}_M E^{-1}(C)$. This is nonempty and open. For $q\in\overline A$, closedness of $C$ gives $E(q)\in C$; in a sufficiently small connected neighborhood $B$ of $q$, take a regular analytic local defining function $h$ for $C$. The function $h\circ E$ vanishes on the nonempty open set $A\cap B$, hence on $B$ by the analytic identity theorem. Thus $A$ is closed and $A=M$.

Distinct periodic trajectories are disjoint by ODE uniqueness, so they cannot occupy this same component. This [continuation mechanism][injection] is checked. Remote points of $M$ need not represent physical passages; the argument only requires an analytic manifold throughout the minor chart and physical interpretation near the initial target. Imposing an additional unlisted physical-cell restriction would require a new completeness argument.

## 10. The complete interface to Theorem 11.2

For each of finitely many words and maximal-minor charts, supply: (i) one fixed analytic system and domain; (ii) positive-margin completeness, including the squared minor margin; (iii) (C-AZP) for its full finite closure, including generated coordinates, derivatives, specializations and determinant restrictions; and (iv) the rank and injection contract above. The projection theorem then supplies a finite constant $N_{w,\nu}$ uniform in the parameter tuple. A finite sum of these constants, plus the degree-dependent exceptional count, bounds the hyperbolic cycles in the fixed geometric domain. Multiple representations only cause overcounting and do not invalidate this upper bound.

This separates the logical quantifiers: the geometric list of words and systems is fixed first; (C-AZP) is verified for an arbitrary fixed generated system using a sequence-dependent but fixed finite enlargement; only then does Theorem 11.2 produce uniform component bounds. Its induction needs hereditary closure, not a uniform numerical bound over every possible generated equation. See the [projection theorem and closure definition][projection].

## 11. Executable audit ledger

| ID | Deliverable required to close the obligation | Pass criterion | Failure criterion | Current status |
| --- | --- | --- | --- | --- |
| C1 | One complete derivative graph for a subdivided old transfer, through order two | Chain rule and implicit jets agree as functions on an open old domain | Agreement only after imposing matching equations | Local algebra checked; primitive identity assumed |
| C2 | Denominator ledger for two successive projection multiplier constructions | Every inverse has a retained nonzero restriction; all equations become finite jet numerators | A dropped divisor, altered inequality, or unlisted primitive evaluation | General finite closure checked |
| C3 | Boundary table for each independent terminal kernel | Every bounded enlarged corner has a common analytic extension and proved state room | A bounded corner where the actual independent flow leaves its analytic state box | Source coverage located; estimates not certified |
| C4 | A fixed subdivision for each bounded-ratio limit | One finite $K$ and one identity apply eventually on the subsequence | Point-dependent unbounded $K_i$ remains necessary | Quantifier contract checked; ODE estimates assumed |
| C5 | A common flag for all kernels of an arbitrary fixed generated system | All derivatives, graph ties, margins and algebraic factors are represented simultaneously | One required factor lacks the primitive contract | Conditional on §§2–8 and §10 |
| C6 | Recovery identity after every graph and chart step | An explicit left inverse for one retained old free input, with all graph equations kept | Free variation is solely an undetermined auxiliary fiber direction | Graph argument checked; elimination invariant assumed |
| C7 | Fixed-parameter rank and component injection | Ambient mismatch identity, invertible graph block, and analytic continuation on each minor chart | Orbit-dependent external parameters, rank inferred only on a locus, or an unlisted global restriction | Linear algebra and continuation checked; geometric realization assumed |

No confirmed flaw is recorded in these local closure arguments. The unresolved entries are proof obligations, not findings that the manuscript is false. Passing them would still leave the upstream separation and elimination estimates, and the geometric finite-family reduction, to be independently audited.

[absolute]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/05-elimination.tex#L1038-L1136
[closure-start]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L705-L722
[graph-jet]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L551-L600
[derivatives]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L750-L767
[clear]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L611-L667
[corners]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/10-terminal.tex#L948-L1130
[bounded]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L769-L836
[divergent]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L838-L879
[finite-k]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L602-L609
[recovery]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L669-L703
[parameters]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L297-L315
[rank]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L447-L499
[injection]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L501-L538
[projection]: https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L22-L217
