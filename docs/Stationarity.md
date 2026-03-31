## Technical Definition

A stochastic process $\{X_t, t \in \mathbb{Z}\}$ is said to be **Strictly Stationary** if the joint distribution of $(X_{t_1}, \dots, X_{t_n})$ is identical to the joint distribution of $(X_{t_1+h}, \dots, X_{t_n+h})$ for all $n$, all time points $t_i$, and all time shifts $h$.

In most applied contexts, we use **Weak Stationarity** (also known as Covariance Stationarity or Second-Order Stationarity). A process is weakly stationary if it satisfies three conditions: 

1. **Constant Mean:** The expected value is independent of time:    

<div class="arithmatex">
\[
E[X_t] = \mu \quad \forall t
\]
</div>

2. **Finite Variance:** The variance is finite and constant for all $t$:    

<div class="arithmatex">
\[
Var(X_t) = \sigma^2 < \infty
\]
</div>

3. **Constant Autocovariance:** The covariance between two observations depends only on the time lag $h$, not on the actual time $t$:    

<div class="arithmatex">
\[
\gamma(h) = Cov(X_t, X_{t+h}) = E[(X_t - \mu)(X_{t+h} - \mu)]
\]
</div>


## Layperson's Definition

In Kenya, mangos are in season from January to March every year. During this period the sales of mangos are higher than all other months in the year. Therefore, data collected on the sales of mangos from year over year aggregated by month will have seasonality and be non stationary. It is important to note of course that even though seasonal data is always non stationary; non stationary data does not imply seasonality.

This is because it violates the three assumptions of weak stationarity. Firstly, the expected value is dependent of time. If I select the time period January to March and compare it with another time period August to October I will find that the former period will have a higher mean sales than the latter. Hence, the distribution is dependent on time. Selecting a different time period leads to a different mean value of the sales.

Secondly, although the variance is finite it is not constant for all time $t$. This is evidenced by the fact that during the months where mangos are in season a large quantity of mangos are sold. The variance in the sales of the mangos is larger. However, when mangos are no longer in season, sales show less variance. This is an exhibition of **heteroscedasticity**.

Finally, the covariance between two observations depends on the actual time $t$ and not only on the time lag $h$. If the time lag is selected as $h =1$, that is a one month lag (pick months that are 1 month apart) depending on the months of the year that one selects in order to get covariance, the values obtained will be different. If covariance is done between January and February (peak season) it will be different than the covariance for August and September (off season). Even though the lag is the same $h = 1$ the covariance is different.

| Year | Month | Mango Sales (Units) | Context/Observation |
| :--- | :--- | :--- | :--- |
| 2023 | Jan | 850 | **Peak Season (High Mean)** |
| 2023 | Feb | 920 | **Peak Season** |
| 2023 | Mar | 780 | **Peak Season** |
| 2023 | Apr | 210 | Mean drops significantly |
| 2023 | May | 185 | Off-season (Low variance) |
| 2023 | Jun-Dec| 150 - 200 | Consistent Low Sales |
| 2024 | Jan | 890 | **Seasonality Repeats** |
| 2024 | Feb | 950 | **Peak Season** |
| 2024 | Mar | 810 | **Peak Season** |
| 2024 | Apr-Dec| 160 - 220 | Off-season |
| 2025 | Jan | 910 | **Mean is Time-Dependent** |
| 2025 | Feb | 980 | **Peak Season** |
| 2025 | Mar | 840 | **Peak Season** |
| 2025 | Apr-Dec| 170 - 230 | Off-season |

On the other hand, for a product like table salt its sales are exhibit stationarity. Whether it is January or July, a household typically consumes the same amount of salt. There is no such thing as a salt season. The average sales $(E[X_t​])$ remain consistent month over month. Moreover, the noise in salt sales is very low. There are no massive bulk-buying panics or periods where sales drop to near zero. The fluctuations $(Var(X_t​))$ are small and stable. Finally, the relationship between sales in January and February is statistically identical to the relationship between sales in August and September. The correlation depends only on the time gap, not the specific month.

| Year | Month   | Salt Sales (Units) | Context/Observation           |
| :--- | :------ | :----------------- | :---------------------------- |
| 2023 | Jan     | 502                | Mean $\approx$ 500            |
| 2023 | Feb     | 498                | Variance is constant          |
| 2023 | Mar     | 505                | Noise is random               |
| 2023 | Apr     | 497                | No seasonal shift             |
| 2023 | May     | 503                | No seasonal shift             |
| 2023 | Jun-Dec | 495 - 508          | Fluctuates around the mean    |
| 2024 | Jan     | 499                | **Mean is Time-Independent**  |
| 2024 | Feb     | 503                | **Constant Variance**         |
| 2024 | Mar     | 501                | **Constant Autocovariance**   |
| 2024 | Apr-Dec | 496 - 505          | Stationary behavior           |
| 2025 | Jan     | 506                | Statistics do not change      |
| 2025 | Feb     | 496                | Statistics do not change      |
| 2025 | Mar     | 500                | Statistics do not change      |
| 2025 | Apr-Dec | 498 - 505          | **Ready for Linear Modeling** |
