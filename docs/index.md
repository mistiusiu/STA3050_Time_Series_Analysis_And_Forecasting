# Seasonal ARIMA (SARIMA) Forecasting

Welcome to our group presentation on **SARIMA*- modeling. This documentation covers the theoretical foundations, mathematical proofs, and the integrated components required to forecast seasonal time series data.

## Presentation Roadmap

### Foundations
Before we can build a SARIMA model, we must understand the core behavior of time series data.

- **[Stationarity](Stationarity.md)**: Understanding mean, variance, and the importance of differencing.

### Building Blocks (Non-Seasonal)
SARIMA is built upon three fundamental processes:  

- **[AR Model (Autoregressive)](AR%20Model.md)**: Predicting future values based on past values.   
- **[MA Model (Moving Average)](MA%20Model.md)**: Predicting future values based on past forecast errors.   
- **[ARMA Model](ARMA%20Model.md)**: Combining AR and MA for stationary series.   
- **[ARIMA Model](ARIMA%20Model.md)**: Introducing Integration ($d$) to handle non-stationary data.   

### The Seasonal Component
- **[Seasonal ARIMA (SARIMA) Model](Seasonal%20ARIMA%20Model.md)**: Extending ARIMA to account for seasonality $(P, D, Q)_s$.  

### Mathematical Rigor
- **[Mathematical Proofs](Mathematical%20Proofs.md)**: Deep dive into the backshift operator $B$, characteristic equations, and derivation of the SARIMA $(p,d,q) \times (P,D,Q)_s$ formula.   
