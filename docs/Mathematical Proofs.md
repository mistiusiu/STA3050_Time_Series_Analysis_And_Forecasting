## Backshift Operator

The Backshift operator $B^n$ mathematically denotes the $n^{th}$ value that precedes the current value. When examining the sales of mangos aggregated by month to denote the sales of two months ago (January 2026) given the current month is March 2026, $B^{2}x_t$ is used. With:


<div class="arithmatex">
\[
B^{2}x_t = x_{t-2}
\]
</div>

The backshift operator exists as a mathematical notation that exists for the sake of convenience of denotation.

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
