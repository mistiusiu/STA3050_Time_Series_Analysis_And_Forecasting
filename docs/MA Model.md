The $MA(q)$ model is expressed as:


<div class="arithmatex">
\[
\quad X_t = \mu + w_t + \theta_1 w_{t-1} + \theta_2 w_{t-2} + \cdots + \theta_q w_{t-q}
\]
</div>

With the values of $w_t$ being normally distributed with mean 0 and a constant variance.


<div class="arithmatex">
\[
w_t \sim \text{i.i.d. } \mathcal{N}(0, \sigma_w^2)
\]
</div>


The theoretical properties are

<div class="arithmatex">
\[
{E}[X_t] = \mu
\]
</div>


<div class="arithmatex">
\[
\operatorname{Var}(X_t) = \sigma_w^2 \left(1 + \theta_1^2 + \theta_2^2 + \cdots + \theta_q^2 \right)
\]
</div>


<div class="arithmatex">
\[
\gamma(h) =  
\begin{cases}  
\sigma_w^2 \displaystyle\sum_{j=0}^{q-h} \theta_j \theta_{j+h}, & 0 \le h \le q \\  
0, & h > q  
\end{cases}
\]
</div>


<div class="arithmatex">
\[
\theta_0 = 1
\]
</div>


To compute the autocorrelation function


<div class="arithmatex">
\[
\rho(h) = \frac{Covariance\ for\ lag\ h}{Variance} =  \frac{\gamma(h)}{\gamma(0)}
\]
</div>


The $MA(q)$ exhibits a slight structural similarity to a linear regression model without an error term. The values of $w_t$ are recursively computed from the observed values of $\mu$ and $\theta_q$. The $\theta$ parameters must be $|\theta| < 1$ to satisfy the [[Mathematical Proofs#Invertibility|invertibility]] condition. This ensures that the current error $w_t$ can be rewritten as a sum of past observed values.

Given that three errors are used $w_1$, $w_2$, and $w_3$; they are initially set to zero and recursively updated.


<div class="arithmatex">
\[
w_1 = X_1 - \mu
\]
</div>


<div class="arithmatex">
\[
w_2 = X_2 - \mu - \theta_1 w_1
\]
</div>


<div class="arithmatex">
\[
w_3 = X_3 - \mu - \theta_1 w_2 - \theta_2 w_1
\]
</div>


With the general form being


<div class="arithmatex">
\[
w_t = X_t - \mu - \sum_{i=1}^{q} \theta_i w_{t-i}
\]
</div>


These weights are then fed back into the model and an algorithm (like Newton-Raphson or Kalman Filtering) adjusts the $\theta$ coefficients and the $\mu$ value repeatedly until the resulting sequence of $w_t$ values minimizes the sum of squared residuals or maximizes the likelihood of the observed data.

The values of $w_t$ are not measured. One assumes a probability distribution, estimates the model coefficients that best fit your data, and then treat the leftover difference between the model's prediction and the actual value as the determined $w_t$.