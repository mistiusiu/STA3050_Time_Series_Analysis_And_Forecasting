## Backshift Operator

The Backshift operator $B^n$ mathematically denotes the $n^{th}$ value that precedes the current value. When examining the sales of mangos aggregated by month to denote the sales of two months ago (January 2026) given the current month is March 2026, $B^{2}x_t$ is used. With:


<div class="arithmatex">
\[
B^{2}x_t = x_{t-2}
\]
</div>

The backshift operator exists as a mathematical notation that exists for the sake of convenience of denotation.

## Invertibility

## Method of Telescoping Sums

Let the partial sum $S_n$​ be the sum of the first n terms of the geometric series:


<div class="arithmatex">
\[
S_n = 1 + \phi + \phi^2 + \phi^3 + \dots + \phi^{n-1}
\]
</div>


Multiply the entire equation by $\phi$:


<div class="arithmatex">
\[
\phi S_n = \phi + \phi^2 + \phi^3 + \phi^4 + \dots + \phi^n
\]
</div>


Subtract the two equations:


<div class="arithmatex">
\[
S_n - \phi S_n = (1 + \phi + \phi^2 + \dots + \phi^{n-1}) - (\phi + \phi^2 + \dots + \phi^n)
\]
</div>


<div class="arithmatex">
\[
S_n(1 - \phi) = 1 - \phi^n
\]
</div>


Solve for $S_n$ by dividing both sides by $(1 - \phi)$:


<div class="arithmatex">
\[
S_n = \frac{1 - \phi^n}{1 - \phi}
\]
</div>


Take the limit as $n \to \infty$. Note that $|\phi| < 1$.


<div class="arithmatex">
\[
\lim_{n \to \infty} \phi^n = 0
\]
</div>


<div class="arithmatex">
\[
S_{\infty} = \frac{1 - 0}{1 - \phi} = \frac{1}{1 - \phi}
\]
</div>


Multiply with the constant $c$.


<div class="arithmatex">
\[
c \times \frac{1}{1 - \phi} = \frac{c}{1 - \phi}
\]
</div>


## White Noise

In every model the white noise $\epsilon_t$ is modeled as a normal distribution with:


<div class="arithmatex">
\[
E[ε_t] = 0
\]
</div>


<div class="arithmatex">
\[
Var(\epsilon_t) = \sigma^2
\]
</div>


<div class="arithmatex">
\[
Cov(ε_t, ε_s) = 0\ for\ t ≠ s
\]
</div>


This effectively means that in the long run when proving theoretical representations of models its effect is effectually zero. In practice, however, it contributes but at the end of the simulation yields a net zero effect. For example, the values of $\epsilon_t$ yielded for a simulation in an idealistic theoretical case would be `[+2, -5, +3, -6, +6]`. However, in real world data this is not the case.

In real world data, the property of an expected value of zero represents that the white noise is unbiased. Its effect is a purely random shock present from the constant time independent value $\sigma^2$. The white noise represents the stochastic shocks that drive the variance in the system. It determines the uncertainty in the model but does not shift the center. It prevents the model from converging at a static constant.

### Negating White Noise in AR Model

Without these shocks an $AR(1)$ model with $\phi=0.5$ would decay to the mean of the series $\mu$ and stay there forever. 


<div class="arithmatex">
\[
Y_t = c + \phi Y_{t-1} + \epsilon_t
\]
</div>


<div class="arithmatex">
\[
Y_1 = c + \phi Y_0
\]
</div>


<div class="arithmatex">
\[
Y_2 = c + \phi(c + \phi Y_0) = c + c\phi + \phi^2 Y_0
\]
</div>


<div class="arithmatex">
\[
Y_3 = c + \phi(c + c\phi + \phi^2 Y_0) = c + c\phi + c\phi^2 + \phi^3 Y_0
\]
</div>

The general form becomes:


<div class="arithmatex">
\[
Y_t = c \sum_{i=0}^{t-1} \phi^i + \phi^t Y_0
\]
</div>

 Since the process is stationary $(|\phi| < 1)$ as $t \to \infty$:


<div class="arithmatex">
\[
\lim_{t \to \infty} \phi^t Y_0 = 0
\]
</div>


<div class="arithmatex">
\[
\lim_{t \to \infty} c \sum_{i=0}^{t-1} \phi^i = \frac{c}{1 - \phi}
\]
</div>

 This causes the deterministic long run mean:


<div class="arithmatex">
\[
\mu = \frac{c}{1 - \phi}
\]
</div>


The convergence of the series is the [[Mathematical Proofs#Method of Telescoping Sums|method of telescoping sums]].

### Vieta's Formulas for AR(2) Model

If a polynomial has roots $z_1$ and $z_2$ then it can be written as a product of its powers. Given the equation for $AR(2)$ starts with 1 $1 - \phi_1B - \phi_2B^2 = 0$ it is written as:


<div class="arithmatex">
\[
(1 - \frac{1}{z_1}B)(1 - \frac{1}{z_2}B) = 0
\]
</div>


Expanding the factors:


<div class="arithmatex">
\[
1 - \frac{1}{z_2}B - \frac{1}{z_1}B + (\frac{1}{z_1})(\frac{1}{z_2})B^2 = 0
\]
</div>


<div class="arithmatex">
\[
1 - (\frac{1}{z_1} + \frac{1}{z_2})B + (\frac{1}{z_1 z_2})B^2 = 0
\]
</div>


Matching the coefficients:


<div class="arithmatex">
\[
1 - \phi_1 B - \phi_2 B^2
\]
</div>


<div class="arithmatex">
\[
\phi_1 = \frac{1}{z_1} + \frac{1}{z_2}
\]
</div>


<div class="arithmatex">
\[
\phi_2 = -\frac{1}{z_1 z_2}
\]
</div>

This links to stationarity since for the distribution to be stationary both $|z_1|$, $|z_2| > 1$ (roots outside the unit circle) this forces the reciprocals 


<div class="arithmatex">
\[
|\frac{1}{z_1}|, |\frac{1}{z_2}| < 1
\]
</div>

Since $\phi_2$ is the negative product of these fractions

<div class="arithmatex">
\[
|\phi_2| < 1
\]
</div>


## Equivalence of Centered and Non-Centered AR(1)

The centered form


<div class="arithmatex">
\[
(1 - \phi_1 B)(Y_t - \mu) = \epsilon_t
\]
</div>

When expanded becomes


<div class="arithmatex">
\[
Y_t - \mu - \phi_1 Y_{t-1} + \phi_1 \mu = \epsilon_t
\]
</div>

By isolating $Y_t$


<div class="arithmatex">
\[
Y_t: Y_t = \mu(1 - \phi_1) + \phi_1 Y_{t-1} + \epsilon_t
\]
</div>

Comparing with the non-centered form


<div class="arithmatex">
\[
Y_t = c + \phi_1 Y_{t-1} + \epsilon_t
\]
</div>

From the [[Mathematical Proofs#Negating White Noise in AR Model|deterministic long run mean]]


<div class="arithmatex">
\[
c = \mu(1 - \phi_1)
\]
</div>


## Orders in Statistics

In algebra the phrase *"order"* refers to exponentiation ($X^2$, $X^3$) but in statistics and time series **polynomial order** refers to power ($X^n$) while **autoregressive order** refers to the lag distance $X_{t-n}$ .

## Differencing
### Seasonal Differencing

In non-stationary data where there is seasonality, the sales of mangos in the Kenyan market for example there is a peak from January to March and a corresponding dip during the remaining months. Seasonal differencing uncovers the span of time it takes for this pattern to repeat (12 months in this case) and shifts the focus from "How much did I sell?" which yields a non-stationary distribution to "How much more or less did I sell compared to the same time last year?" which yields a stationary distribution. Seasonal differencing performs the simple subtraction of (given `S = 12`):


<div class="arithmatex">
\[
x_t - x_{t-12}
\]
</div>

It subtracts the value this year with the value last year. If the sales in January 2024 were 900 (in thousands of Kenyan shillings) and the sales in January 2025 were 900 (in thousands of Kenyan shillings) then the differenced value is 0. In a more realistic scenario the sales in the January time slice from 2001 to 2010 could be:

| Year | Month | Raw Jan Sales | Seasonal Difference | Interpretation             |
| :--- | :---- | :------------ | :------------------ | :------------------------- |
| 2001 | Jan   | 800           | -                   | Baseline                   |
| 2002 | Jan   | 815           | **+15**             | Slight growth              |
| 2003 | Jan   | 828           | **+13**             | Consistent growth          |
| 2004 | Jan   | 845           | **+17**             | Constant Mean $\approx$ 15 |
| 2005 | Jan   | 858           | **+13**             | Constant Variance          |
| 2006 | Jan   | 875           | **+17**             | Stationary Noise           |
| 2007 | Jan   | 890           | **+15**             | Independent of $t$         |
| 2008 | Jan   | 906           | **+16**             | Stable Fluctuations        |
| 2009 | Jan   | 920           | **+14**             | Predictable growth         |
| 2010 | Jan   | 936           | **+16**             | **Stationary Series**      |

The seasonal differenced values shows a constant mean of $\approx$ 15 displaying a (weakly) stationary series. The variance and covariance are also constant and independent of time. In this case, despite the fact that the mango trader is consistently making higher profits year over year in January the plotted differenced values exhibit stationarity. In practice, business profits might typically grow year over year but their growth trajectory (assuming the only component affecting stationarity is seasonality) will be stationary. In actuality, even after seasonal differencing the resultant distribution might not be stationary yet hence requiring further mathematical manipulations.

## Non - Stationary Series
### Mean
In non stationary data like the mango sales the mean is a function that changes with time (rather than being a single value like in the tablsalt stationary data). Raw data can be modeled as:


<div class="arithmatex">
\[
x_t = \mu_{t} + \epsilon_{t}
\]
</div>


where $\mu_{t} = T_t + S_t$ .

In the mango sales example the trend ($T_t$) is the long-term upward crawl in sales from more people moving into Nairobi due to rural-urban migration year over year. The periodic component ($S_t$) is the seasonal humps (January to March peak season).

When non-stationary data is differenced ideally if all trend and seasonality components are identified and removed the mean function effectively becomes 0 hence the mean is eliminated leaving only the normally distributed errors.
