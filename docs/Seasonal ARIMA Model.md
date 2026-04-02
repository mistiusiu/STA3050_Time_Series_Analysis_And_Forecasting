## Preamble

Before exploring this content ensure that you have brushed up on [[Stationarity]] , [[AR Model]], [[MA Model]], [[ARMA Model]],  and the [[ARIMA Model]]. If any mathematical notation or expansion feels unfamiliar explore the linked [[Mathematical Proofs|proofs]] content.

## Introduction

In a seasonal ARIMA model, seasonal AR and MA terms predict $x_t$ using data values and errors that are multiples of S (the span of the seasonality).

For example, if `S = 12` and $x_t$ is March 2026 then a seasonal first order autoregressive model AR(1) will use $x_{t-12}$ to predict $x_t$ where $x_{t-12}$ is March 2025. Similarly, a second order autoregressive model AR(2) will use $x_{t-12}$ and $x_{t-24}$ to predict $x_t$. Hence it will use March 2025 and March 2024. In the same vein, a seasonal first order moving average and second order moving average model, MA(1) and MA(2) respectively, will use $w_{t-12}$, and $w_{t-12}$ and $w_{t-24}$ respectively to predict $w_{t}$.

## Differencing

Seasonality often causes data to lack stationarity (not be stationary). This is because the average values at some particular times within the seasonal span (months, for example) may be different that the mean values at other times. Fruits are in season chiefly during certain months in a year. Mangos are usually in season during the first few months of the year in Kenya (January to March) hence their sales during this time will be higher than in the other months where they are not in season.

### Seasonal Differencing

With `S = 12`, which may occur with monthly data, a seasonal difference using the [[Mathematical Proofs#Backshift Operator|Backshift Operator]] would be:


<div class="arithmatex">
\[
(1 - B^{12})x_t = x_t - x_{t-12}
\]
</div>


The logic behind this differencing is that since the patterns in the data are observed to repeat every `S` spans of time, it stands to reason that in the case of `S = 12` where we are dealing with months; the values (differences) in the previous year may be about the same for each month of the year yielding a stationary series. This removes the seasonal trend and can also get rid of a seasonal random walk type of stationarity ([[Mathematical Proofs#Seasonal Differencing|Proof]]).

#### Importance of Seasonal Differencing

Seasonal differencing eliminates the seasonal patterns. The mango sales data during peak mango season is a seasonal pattern that repeats every 12 months. A non-seasonal differencing cannot eliminate such a pattern. Only the general trend is eliminated but the seasonal peaks remain.

Moreover, when a time series' present value is strongly linked with its value from the same season in the prior year, it has a seasonal unit root. In mango sales data the peak season is January (to March). Thus, the sales in January 2026 are strongly influenced by the sales in January 2025. A seasonal unit root represents that the value of $|\Phi| = 1$ meaning it falls within the unit circle. This means that the sales of consecutive years is the sale of the previous years plus a shock causing the effect to diverge towards infinity exhibiting non-stationarity. However, in a stationary series that is effected by shifting the question from "What are my sales in January 2026?" to "How many more or less mangos did I sell this January (2026) compared to January last year (2025)?". This can only be stabilized by
seasonal differencing, not by standard differencing. This is further explored in [[Stationarity|stationarity]].

Hence, seasonal differencing creates a stationary seasonal pattern. This converts data with multiplicative seasonality into an additive stationary form.

### Non-Seasonal Differencing

If trend is present in the data then there is need for non-seasonal differencing to remove the trend present in the data. Hence we use:


<div class="arithmatex">
\[
(1 - B)x_t = x_t - x_{t-1}
\]
</div>


### Differencing for Trend and Seasonality

If both trend and seasonality are present then the ACF and PACF of:


<div class="arithmatex">
\[
(1 - B^{12})(1 - B)x_t = (x_t - x_{t- 1)} - (x_{t-12} - x_{t - 13})
\]
</div>

ought to be examined. This effectively breaks down the dependency into recent things that have happened and long-range things that have happened using these to assume that the sales of mangos in the current month (going back to the mangos) example can be explained by the sales in the previous month (recent things) and the sales from the same month a year ago (long-range things). The mean, $\mu_{t}$, may have been removed part of which may include a periodic component ([[Mathematical Proofs#Mean|Proof]]).

By examining the ACF and PACF behavior over the first few lags (less than S) the non-seasonal terms that might work in further refining the model can be determined (the ACF and PACF plots effectively plot the residuals). A case in point is if the ACF still shows huge spikes at lag 12, it means the periodic component wasn't fully removed, and you might need a more complex seasonal model (like a Seasonal MA term).

## Patterns in ACF and PACF

The autocorrelation function (ACF) measures the correlation between observations separated by different time lags. If data has seasonality, the ACF will exhibit significant spikes at seasonal lags ($S$, $2S$, $3S$). For the mango sales data ($S = 12$), this means strong spikes at lags 12 and 24. A gradual decay in the seasonal lags suggests seasonal non-stationarity of the data requiring seasonal differencing ($D$). A sharp cutoff at seasonal lags suggests the presence of a seasonal MA component. Hence, ACF is used to identify the non-seasonal MA order ($q$) at early lags and the seasonal MA order ($Q$) at seasonal lags.

The partial autocorrelation function (PACF) measures the direct correlation between observations after removing the effects of intermediate lag variables. It effectually asks the question _"Does knowing what happened two days ago tell me anything that knowing what happened yesterday didn't already cover?"_. If the answer is no then the PACF is 0. 

If data has seasonality, the PACF will exhibit significant spikes at seasonal lags ($S$, $2S$, $3S$). For the mango sales data ($S = 12$), this means strong spikes at lags 12 and 24. A gradual decay in the seasonal lags suggests seasonal non-stationarity of the data requiring seasonal differencing ($D$). A sharp cutoff at seasonal lags suggests the presence of a seasonal AR component ($P$). The identified AR order that will remove the non-seasonal and seasonal non stationary effects is the last lag before the PACF spikes "cut off" and hit the blue significance zone. Hence, ACF is used to identify the non-seasonal MA order ($p$) at early lags and the seasonal MA order ($P$) at seasonal lags.

To illustrate this $MA(1)$ and $MA(2)$ models will be simulated.

![Simulated MA(1) data](https://online.stat.psu.edu/stat510/Lesson02_files/figure-html/fig-simulatedMA1-1.png)

The ACF plot is

![ACF for simulated MA(1) data](https://online.stat.psu.edu/stat510/Lesson02_files/figure-html/fig-ACFsimulated-1.png)

For $MA(2)$

![Simulated MA(2) Series](https://online.stat.psu.edu/stat510/Lesson02_files/figure-html/fig-simulatedtimeseries-1.png)

![ACF for simulated MA(2) Data](https://online.stat.psu.edu/stat510/Lesson02_files/figure-html/fig-ACFforma2-1.png)

## Model Notation

Seasonal and non-seasonal components are incorporated in a multiplicative model.


<div class="arithmatex">
\[
ARIMA(p, d, q) \times (P, D, Q)S
\]
</div>

$p$ = non-seasonal AR order   
$d$ = non-seasonal differencing   
$q$ = non-seasonal MA order   
$P$ = seasonal AR order    
$D$ = seasonal differencing    
$Q$ = seasonal MA order   
$S$  = time span of repeating seasonal pattern    

The Seasonal ARIMA model is two separate ARIMA models multiplied together. The first one handles the relationship between two consecutive points (months for our mango sales) and the other handles the same points across seasons (years for our mango sales).

The aim of the SARIMA model is to effectively locate coefficients that turn the data into uncorrelated white noise.

In the case where there is no differencing parameter achieving such an operation will cause:


<div class="arithmatex">
\[
AR\ Side \times Data = MA\ Side \times Noise
\]
</div>

By passing the data though an autoregressive filter it subtracts out everything that can be predicted from the past leaving behind the unpredictable parts of the data. By adding the memory of past shocks to the pure white noise $\epsilon_t$ this causes structured randomness to result. If the two sides are equal then the model has accounted for every pattern in the data, leaving only the unaccountable noise.

The Data ($Y_t$) is modeled as filtered noise being a weighted collection of current and past random shocks.


<div class="arithmatex">
\[
Y_t = \frac{MA\ Side}{AR\ Side} \times Noise
\]
</div>

We could also solve for the noise:


<div class="arithmatex">
\[
\epsilon_t = \frac{MA\ Side}{AR\ Side} \times Y_t
\]
</div>

The mathematical notation for the AR and MA sides is:


<div class="arithmatex">
\[
\underbrace{\Phi_P(B^S) \phi_p(B)}_{\text{Combined AR}} (Y_t - \mu) = \underbrace{\Theta_Q(B^S) \theta_q(B)}_{\text{Combined MA}} \epsilon_t
\]
</div>


| Component           | Algebraic Operator | What it represents                                               |
| :------------------ | :----------------- | :--------------------------------------------------------------- |
| **Non-seasonal AR** | $\phi_p(B)$        | $(1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p)$               |
| **Seasonal AR**     | $\Phi_P(B^S)$      | $(1 - \Phi_1 B^S - \Phi_2 B^{2S} - \dots - \Phi_P B^{PS})$       |
| **Non-seasonal MA** | $\theta_q(B)$      | $(1 + \theta_1 B + \theta_2 B^2 + \dots + \theta_q B^q)$         |
| **Seasonal MA**     | $\Theta_Q(B^S)$    | $(1 + \Theta_1 B^S + \Theta_2 B^{2S} + \dots + \Theta_Q B^{QS})$ |

Note that in this notation there is no constant $c$. This occurs from the choice to subtract $\mu$ from the data. This centers the data enabling easier computations (working with as series with a mean of 0 is easier) and not requiring the constant $c$ to be carried in all computations. The [[Mathematical Proofs#Equivalence of Centered and Non-Centered AR(1)|equivalence of the centered and non-centered AR]]  causes:


<div class="arithmatex">
\[
\phi(B)(Y_t - \mu) = \epsilon_t
\]
</div>


<div class="arithmatex">
\[
\phi(B)Y_t = c + \epsilon_t
\]
</div>

## Assumptions
### Stationarity After Differencing

After applying regular and seasonal differencing, the series must have a constant mean and constant autocovariance that depends only on lag $h$, not on time $t$. This is the mathematical foundation of SARIMA modeling. Mombasa tea prices often exhibit an upward trend due to inflation and global demand, and seasonal peaks after harvests. Differencing removes the trend and stabilizes the seasonal pattern. If the variance grows over time (price volatility increases with inflation), this assumption fails.

### White Noise Residuals

The errors left after fitting the model must be completely random with zero mean, no autocorrelation, and constant variance. This confirms the model has captured all predictable patterns. After modeling tea prices, if residuals still show correlation at 12-month lags, the model has missed part of the seasonal structure—perhaps a secondary seasonal effect.

### Constant Variance of Residuals

The spread of prediction errors should remain consistent across all time periods and levels of predicted values. If the model predicts tea prices poorly during volatile periods like drought years but well during stable years, variance is not constant. A logarithmic or box-cox transformation may be needed before modeling.

### Normality of Residuals

The errors should follow a bell-shaped distribution. While point forecasts remain reliable without normality, this assumption is essential for valid confidence intervals, hypothesis tests, and prediction intervals. If there are extreme price spikes, like a sudden 50% price jump due to a major buyer entering the market, create heavy-tailed residuals, prediction intervals will be unreliable even if point forecasts are acceptable.

### Linearity

SARIMA assumes that future values are a linear combination of past values and past errors. It cannot capture nonlinear relationships, threshold effects, or regime switches. Tea prices may respond differently to a rainfall deficit depending on whether the market is already in a supply glut. SARIMA cannot capture such nonlinear dynamics.

### Fixed and Known Seasonal Period

You must know the length of the seasonal cycle in advance, and that length must remain constant. For monthly tea data, the seasonal period is 12. If tea harvesting patterns shift due to climate change, for instance, two rainy seasons merging into one, the fixed 12-month seasonality no longer aligns with reality.

### Stable Seasonal Pattern

The strength and shape of the seasonal pattern must remain consistent over time. Seasonal peaks and troughs should maintain similar magnitude and timing. If climate change causes the main tea harvest to shift from June to May over a decade, the seasonal pattern is not stable. SARIMA would misalign over time.

### No Structural Breaks

The underlying process generating the data must remain stable throughout the period. SARIMA cannot handle sudden policy changes, major economic events, changes in trend direction, or shifts in seasonal behavior. In 2023, Kenya introduced a new tea auction floor system that altered price-discovery mechanisms. Such a structural break violates the assumption of a stable data-generating process. Hence, SARIMA models trained with data predating 2023 would struggle to predict prices post 2023.

### No Outliers or Level Shifts

The data should not contain extreme observations or sudden jumps to new levels that do not revert. A single outlier, such as a month where prices doubled due to a panic buy by a major importer, can distort parameter estimates and create misleading autocorrelation patterns.

## Limitations
### Manual Specification Complexity

Selecting the correct combination of parameters $(p, d, q, P, D, Q, s)$ requires experience and careful analysis. The search space is enormous, and poor choices lead to underfitting or overfitting. A novice analyst might choose the wrong seasonal order for tea prices, failing to capture the post-harvest price dip, resulting in systematic forecast errors.

### Large Data Requirements

SARIMA needs enough data to reliably estimate seasonal patterns, at least four to five full seasonal cycles. For monthly tea data, this means four to five years of observations. If a researcher attempts to model tea prices using only 18 months of data, the seasonal component cannot be reliably estimated.

### Single Seasonality Only

Standard SARIMA can only handle one seasonal pattern at a time. Data with multiple seasonal cycles cannot be adequately modeled without extensions or alternative approaches. If tea prices exhibited both a 12-month cycle and a 6-month intra-year pattern related to two harvest seasons, SARIMA could only model one.

### Forecast Horizon Degradation

Forecasts become increasingly uncertain as you project further into the future. SARIMA works best for short-term forecasting. A SARIMA model may forecast next month's tea price reasonably well but will likely converge to the average seasonal pattern with wide confidence intervals when forecasting two years ahead.

### Univariate Only

Standard SARIMA uses only the past values of the series itself to make predictions. It cannot incorporate external information that might improve forecasts. A model for tea prices would be stronger if it could include rainfall in tea-growing regions, global crude oil prices (affecting transport), or exchange rate movements. Standard SARIMA cannot do this.

### Fixed Parameters

Once estimated, model parameters remain constant over time. The model cannot adapt to gradual changes in trends or evolving seasonal patterns without periodic re-estimation or rolling window approaches. As Kenyan tea gradually gains premium branding in export markets, the long-term price trend may steepen. A SARIMA model estimated a decade ago would not adapt to this change unless re-estimated.

## Overcoming SARIMA's Limitations

### SARIMAX

By including exogeneous variables it overcomes SARIMA's limitations of being univariate only. It will incorporate rainfall data, global tea price index, and fuel costs as exogenous variables to improve forecast accuracy of tea prices. However, it still assumes single seasonality, still requires manual parameter selection, and coefficients remain fixed.

### TBATS (Trigonometric Box-Cox ARMA Trend Seasonal)

It handles multiple seasonal period and allows seasonality to evolve over time. If tea prices show both a 12-month cycle and a secondary 6-month cycle related to two harvest seasons, TBATS can model both simultaneously. It is, however, univariate only and does not easily incorporate external drivers.

### Prophet

It is designed for business forecasting with automatic changepoint detection, multiple seasonalities, and simple tuning. It automatically detects when the price trend shifted due to policy changes like the 2023 auction system change. It also incorporates holiday effects (Ramadan demand spikes), handles yearly and monthly seasonalities, and allows inclusion of weather variables as regressors. It still has a linear additive structure, and may require regularization to avoid overfitting.

## Summary

SARIMA remains a powerful and interpretable model for univariate time series with a single, stable seasonal pattern and no structural breaks. However, for complex real-world data, such as Mombasa tea prices, which may involve multiple seasonalities, external drivers, structural breaks, and evolving seasonal patterns, practitioners should consider SARIMAX, TBATS, or Prophet depending on the specific limitations they face.
