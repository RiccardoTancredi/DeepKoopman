import numpy as np
# import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def hopf_bifurcation(t, z, omega=1.0):
    x, y = z
    mu = mu_value(t) 
    omega = omega
    dzdt = [mu * x - omega * y - (x**2 + y**2) * x,
            omega * x + mu * y - (x**2 + y**2) * y]
    return dzdt

# def mu_value(t):
#     if t % 20 < 10:
#         return -0.5  # Subcritical phase
#     else:
#         return 0.5   # Supercritical phase

def mu_value(t):
    return -0.01  # Subcritical phase


def solve(hopf_bifurcation, t_span, z0, t_eval, args=()):
    if args != None:
        sol = solve_ivp(hopf_bifurcation, t_span, z0, args=(*args,), t_eval=t_eval, method='RK45')
    else:
        sol = solve_ivp(hopf_bifurcation, t_span, z0, t_eval=t_eval, method='RK45')
    x, y = sol.y
    return x, y

# # Parameters
# T = 1_000
# t_span = (0, T)
# dt = 0.1
# tot_range = int(T/dt)
# t_eval = np.linspace(*t_span, tot_range)
# z0 = [0.1, 0.1]  # Initial condition

# # Solve the system with time-varying mu
# sol = solve_ivp(hopf_bifurcation, t_span, z0, t_eval=t_eval, method='RK45')
# x, y = sol.y

# Phase space plot
# fig, axs = plt.subplots(1, 2, figsize=(12, 6))
# axs[0].plot(x, y)
# axs[0].set_title('Phase Space (x-y)')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('y')
# axs[0].grid()

# # Time series plot of x and y
# axs[1].plot(sol.t, x, label='x')
# axs[1].plot(sol.t, y, label='y')
# axs[1].set_title('Time Series')
# axs[1].set_xlabel('Time')
# axs[1].set_ylabel('Values')
# axs[1].legend()
# axs[1].grid()

# plt.tight_layout()
# plt.show()
