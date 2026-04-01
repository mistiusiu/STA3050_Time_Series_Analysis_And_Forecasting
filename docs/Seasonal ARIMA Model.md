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

