Such a model combines $AR(p)$ and $MA(q)$ to form $ARMA(p, q)$. It is expressed as


<div class="arithmatex">
\[
\phi(B)(X_t - \mu) = \theta(B) w_t
\]
</div>

or


<div class="arithmatex">
\[
X_t - \mu = \frac{\theta(B)}{\phi(B)} w_t
\]
</div>

where


<div class="arithmatex">
\[
\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \cdots - \phi_p B^p
\]
</div>



<div class="arithmatex">
\[
\theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \cdots + \theta_q B^q
\]
</div>



<div class="arithmatex">
\[
w_t \sim \text{i.i.d. } \mathcal{N}(0, \sigma_w^2)
\]
</div>


In stationary data $ARMA(p, q)$ combines the understanding that past data influences present data hence capturing momentum and trends ($AR(p)$) and that the current value depends on how wrong we were about previous predictions capturing short-term volatility and noise correction ($MA(q)$). If it was hot yesterday, it is likely to be hot today. Moreover, if a supply chain strike happened two days and that caused us to wrong about the prediction yesterday then the degree to which we were wrong will likely affect today's prediction.

If we planned to sell 600 mangos yesterday but two days ago the delivery trucks were hijacked leading to only 200 mangos being sold then today it is likely that the shock (unexpected variance) will affect the number of mangos sold. Customers expected a lot of mangos yesterday but got few so they might assume today there will be few mangos causing sales to be low. Or delivery people will fear a similar hijacking and not ship mangos.

Moreover, some data requires an infinite $AR$ model to explain it adequately but only a simple $MA$ model and vice versa. ARMA offers the best of worlds describing complex, wiggly data with very few parameters. In data science, fewer parameters usually mean a more robust model that doesn't overfit the noise. ARMA effectively handles the question _"Based on where we were (AR) and the surprises we just had (MA), where are we likely to be right now?"_.