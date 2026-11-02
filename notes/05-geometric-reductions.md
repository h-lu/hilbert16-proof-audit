# Geometric reductions: a finite hyperbolic bound implies a bound for all isolated cycles

**中文导读。** 本节逐步核查一般次数论文的最后两个归约：用同一个带符号旋转，把任意选定的有限个孤立极限环变成至少同样多的双曲极限环；再用空间缩放，把该有限选择移入固定方形。论证不预先假定一个向量场的全部极限环有限。这里核查的是一个条件蕴含，仍须以前文提供的、对所有系数一致的固定方形双曲环上界为输入。

Audit date: 2026-11-02. Primary source: OpenAI, *Uniform bounds for planar polynomial limit cycles*, §11, [rotation lemma and final proof, lines 936–1031](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/11-counting.tex#L936). All manuscript references in this note use commit `4eaee87548250b2682affda7d05d947c05554bae`.

## 1. The precise conditional statement

Fix a degree bound $d$ and a bounded open square $S$. Assume:

> There is a finite number $H_d$, independent of every polynomial coefficient, such that every real polynomial vector field of degree at most $d$ has at most $H_d$ geometrically distinct hyperbolic periodic orbits whose images are contained in $S$.

Then every degree-at-most-$d$ polynomial vector field in the whole plane has at most $\lceil H_d\rceil$ isolated periodic orbits. A limit cycle here is the geometric image of a nonconstant periodic trajectory isolated among such images. Period annuli are not counted as collections of limit cycles.

The quantifier to establish is

$$
\forall V\;\forall N\in\mathbb N\;\forall(C_1,\ldots,C_N),\qquad
\left[\begin{array}{c}
\deg V\le d,\\ C_i\text{ are pairwise distinct limit cycles of }V
\end{array}\right]
\Longrightarrow N\le H_d.
$$

The scaling, the local sections and the permissible perturbation size may depend on this finite selection. The number $H_d$ may not.

## 2. A transverse derivative for the rotation parameter

Let $J(a,b)=(-b,a)$, and use the one-parameter family

$$
V_\mu=V+\mu JV.
$$

Fix one selected cycle, a point $z_0$ on it, and its minimal period $T>0$. The velocity never vanishes along this orbit: a solution reaching an equilibrium would be constant by uniqueness. Consequently the periodic orbit is a regular embedded analytic circle and admits a small transverse section $\sigma(r)$, with $\sigma(0)=z_0$.

Analytic dependence of the local flow and transversality at return give an analytic return time $\tau(r,\mu)$ and an analytic return map $\Pi(r,\mu)$, for $(r,\mu)$ near $(0,0)$. Define

$$
D(r,\mu)=\Pi(r,\mu)-r.
$$

To calculate its parameter derivative, first differentiate the trajectory with fixed starting point and fixed time:

$$
u(t)=\left.\partial_\mu\phi_{V_\mu}(t,z_0)\right|_{\mu=0},
\qquad
u'=DV(z(t))u+JV(z(t)),\qquad u(0)=0.
$$

Set $w(t)=\det(V(z(t)),u(t))$. Since $\frac{d}{dt}V(z(t))=DV(z(t))V(z(t))$, the two-dimensional determinant identity gives

$$
w'=(\operatorname{div}V)(z(t))w+|V(z(t))|^2.
$$

Solving this scalar inhomogeneous equation yields

$$
w(T)=\int_0^T
\exp\!\left(\int_s^T\operatorname{div}V(z(v))\,dv\right)
|V(z(s))|^2\,ds>0.
$$

The actual return point satisfies
$\phi_{V_\mu}(\tau(0,\mu),z_0)=\sigma(\Pi(0,\mu))$.
Its derivative at $\mu=0$ therefore obeys

$$
u(T)+V(z_0)\partial_\mu\tau(0,0)
=\sigma'(0)D_\mu(0,0).
$$

Taking the determinant with $V(z_0)$ eliminates the return-time correction:

$$
\det(V(z_0),\sigma'(0))D_\mu(0,0)=w(T)>0.
$$

The section determinant is nonzero, proving $D_\mu(0,0)\ne0$. Its sign need not be fixed across arbitrary choices of section coordinates; nonvanishing is the required fact.

## 3. Simple roots near a possibly degenerate cycle

The analytic implicit function theorem, applied in the $\mu$ direction, writes the local zero set of $D$ as

$$
\mu=\psi(r),\qquad \psi(0)=0.
$$

Isolation of the original cycle implies that $D(r,0)$ is not the zero germ. Otherwise every sufficiently nearby section point would be fixed, producing nearby periodic orbits. Thus $\psi$ is a nonzero analytic germ and has a finite order:

$$
\psi(r)=a r^m+O(r^{m+1}),\qquad a\ne0,\quad m\ge1.
$$

After shrinking the section interval,

$$
\psi'(r)=r^{m-1}(ma+O(r))\ne0\qquad(0<|r|<\delta).
$$

For odd $m$, the two sides of the interval map to opposite signs of $\mu$; strict monotonicity gives one nearby nonzero root for either sufficiently small nonzero sign. For even $m$, both sides map to the sign of $a$; each side gives one root for that sign. The claim concerns sufficiently small parameter magnitudes, obtained by taking a positive threshold below the relevant endpoint image values.

At each of these roots, differentiating $D(r,\psi(r))=0$ gives

$$
D_r(r,\mu)=-D_\mu(r,\mu)\psi'(r)\ne0.
$$

Continuity preserves $D_\mu\ne0$ in the chosen neighborhood. Hence $\Pi_r\ne1$. The scalar transverse multiplier of a planar flow at a periodic orbit is positive (equivalently, it is the exponential of the divergence integral over that orbit). Therefore $|\Pi_r|\ne1$, which is hyperbolicity, not merely a simple algebraic root condition.

Choose the return construction in a sufficiently thin tubular neighborhood. The usual local Poincaré correspondence identifies its fixed points with nearby one-turn periodic orbits. A transverse section in that tube meets each such orbit once per turn. In particular, the two distinct fixed points created in the even-order case give two distinct geometric orbit images.

## 4. One common sign for a finite selection

Let $C_1,\ldots,C_N$ be any finite selection. Distinct periodic trajectories are disjoint by uniqueness, and each image is compact. We may therefore choose pairwise disjoint tubular neighborhoods and carry out the preceding construction in each.

Let $O$ count the cycles with odd $m$, and let $E_+$ and $E_-$ count those with even $m$ whose favorable signs are positive and negative. For each cycle choose a positive perturbation threshold ensuring the conclusions above and confinement of the resulting orbits to its tube. The minimum of these finitely many thresholds is still positive.

For every sufficiently small common magnitude $\eta>0$, the fields $V_{+\eta}$ and $V_{-\eta}$ have at least, respectively,

$$
O+2E_+\quad\text{and}\quad O+2E_-
$$

hyperbolic cycles in the union of these tubes. Their maximum is at least their average,

$$
O+E_++E_-=N.
$$

This is an aggregate count. It does not require each original cycle to survive for the selected sign. Tubes separate cycles originating from different members of the selection; the section correspondence separates the two cycles originating from one even-order member. Finally,
$V_\mu=(P-\mu Q,Q+\mu P)$, so polynomial degree does not increase.

## 5. Scaling and the finite-witness conclusion

Start with an arbitrary finite selection anywhere in the plane. Its union is compact. A spatial homothety and translation

$$
z=a+Ru,\qquad R>0,
$$

can place all selected orbit images strictly inside $S$. The transformed field is

$$
W(u)=R^{-1}V(a+Ru),
$$

which has degree at most $d$. This coordinate change conjugates the flows without changing time; it preserves nonconstant periodicity, isolation and distinctness. It can change coefficient magnitudes substantially, which is why the input bound must hold for all coefficient values. The manuscript explicitly uses unrestricted coefficient vectors in [§9, lines 4–10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/09-subdivision.tex#L4).

Choose the disjoint tubes with closures contained in $S$, and apply the common-sign result to $W$. A sufficiently small perturbation has at least $N$ hyperbolic cycles in $S$, and still has degree at most $d$. The assumed square bound implies $N\le H_d$.

Thus every finite selection from the full set of limit cycles has uniformly bounded size. If that set had more than $\lceil H_d\rceil$ elements, including if it were infinite, one could select $\lceil H_d\rceil+1$ distinct elements. This contradicts the inequality just proved. No preliminary individual-finiteness theorem is used.

## 6. What remains upstream

The manuscript proposes

$$
H_d=T(d)+\sum_{w\in\mathcal W_d}\sum_I N_{w,I},
$$

using finitely many geometric words and maximal-minor charts, a uniform component bound for each matching system, and an injection from represented hyperbolic cycles into components. This note does not establish that the proposed matching systems possess all required closure and domain properties. It also does not justify exchanging a sequence-dependent subdivision with the degree-dependent finite word list.

The signed-rotation and finite-witness scaling arguments above are sound conditional reductions. They supply neither an independent proof of the finite-template hyperbolic bound nor an effective formula for it. The provenance and limited role of the community expositions are recorded in [06-community-sources.md](06-community-sources.md).
