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

## Model Notation

Seasonal and non-seasonal components are incorporated in a multiplicative model.


<div class="arithmatex">
\[
ARIMA(p, d, q) \times (P, D, Q)S
\]
</div>


### Resources
[PSU Stat 510 Seasonal Models](https://online.stat.psu.edu/stat510/Lesson04)   
[Introduction to SARIMA Model](https://medium.com/@ritusantra/introduction-to-sarima-model-cbb885ceabe8)   
[PSU STAT 510](https://online.stat.psu.edu/stat510/)   
[Time Series Analysis using ARIMA & SARIMA](https://www.kaggle.com/code/pratyushakar/time-series-analysis-using-arima-sarima)   
[Rossman Store Sales](https://www.kaggle.com/c/rossmann-store-sales)    

