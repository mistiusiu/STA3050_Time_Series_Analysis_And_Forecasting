import numpy as np
from scipy.optimize import minimize

def get_ma2_residuals(params, data, mu):
    """Calculates the sequence of w_t based on theta params."""
    theta1, theta2 = params
    w = [0, 0] # Initial conditions
    for x_t in data:
        # Recursive determination: w_t = X_t - mu - theta1*w_{t-1} - theta2*w_{t-2}
        w_t = x_t - mu - (theta1 * w[-1]) - (theta2 * w[-2])
        w.append(w_t)
    return w


def compute_residuals(params, data, mu):
    """
    Given a set of thetas, this calculates the sequence of w_t.
    """
    theta1, theta2 = params
    w = [0, 0]  # Initial conditions w_0, w_{-1}
    
    for x_t in data:
        # Recursive determination: w_t = X_t - mu - theta1*w_{t-1} - theta2*w_{t-2}
        w_t = x_t - mu - (theta1 * w[-1]) - (theta2 * w[-2])
        w.append(w_t)
    
    # Return only the calculated w_t (excluding the initial zeros)
    return np.array(w[2:])

def objective_function(params, data, mu):
    """
    The goal of the optimizer: Minimize the Sum of Squared Errors (SSE).
    """
    residuals = compute_residuals(params, data, mu)
    sse = np.sum(residuals**2)
    return sse

# 1. Setup Data
observations = np.array([12, 8, 11, 10, 9])
mean_mu = 10

# 2. Initial Guess for Thetas (starting point for the iteration)
initial_guess = [0.1, 0.1]

# 3. Run the Optimizer (Convergence Process)
result = minimize(objective_function, initial_guess, args=(observations, mean_mu), method='L-BFGS-B')

# 4. Extract optimized results
opt_theta1, opt_theta2 = result.x
final_w = compute_residuals(result.x, observations, mean_mu)

print(f"Convergence Status: {result.message}")
print(f"Optimized Theta 1: {opt_theta1:.4f}")
print(f"Optimized Theta 2: {opt_theta2:.4f}")
print("-" * 30)
print(f"{'t':<4} | {'X_t':<6} | {'Final w_t':<10}")
for t, (x, w) in enumerate(zip(observations, final_w), 1):
    print(f"{t:<4} | {x:<6} | {w:<10.4f}")

res = minimize(objective_function, [0.1, 0.1], args=(observations, mean_mu))
opt_t1, opt_t2 = res.x

all_w = get_ma2_residuals([opt_t1, opt_t2], observations, mean_mu)
w_T = all_w[-1]    # w_5
w_T_minus_1 = all_w[-2]  # w_4

# 3. Prediction Logic
# X_{T+1} = mu + w_{T+1} + (theta1 * w_T) + (theta2 * w_{T-1})
# Since E[w_{T+1}] = 0:
prediction_T1 = mean_mu + (opt_t1 * w_T) + (opt_t2 * w_T_minus_1)

# X_{T+2} = mu + w_{T+2} + (theta1 * w_{T+1}) + (theta2 * w_T)
# Since E[w_{T+2}] and E[w_{T+1}] = 0:
prediction_T2 = mean_mu + (opt_t2 * w_T)

print(f"Optimized Parameters: θ1={opt_t1:.4f}, θ2={opt_t2:.4f}")
print(f"Last two errors: w_5={w_T:.4f}, w_4={w_T_minus_1:.4f}")
print("-" * 30)
print(f"Prediction for T+1 (Step 6): {prediction_T1:.4f}")
print(f"Prediction for T+2 (Step 7): {prediction_T2:.4f}")
print(f"Prediction for T+3 (Step 8): {mean_mu:.4f} (Reverts to Mean)")
