import numpy as np
import matplotlib.pyplot as pyplot


def euler_chromer(t_vals: np.ndarray, theta_0: float, l: float) -> tuple[np.ndarray, np.ndarray]:
    theta = np.full_like(t_vals, np.deg2rad(theta_0))
    omega = np.zeros_like(t_vals)
    dt = t_vals[1]-t_vals[0]

    for t_i in range(len(t_vals) - 1):
        omega[t_i] = omega[t_i-1] - (9.8/l)*theta[t_i-1]*dt
        theta[t_i] = theta[t_i-1]+omega[t_i]*dt

    return theta


def euler_chromer1(t_vals: np.ndarray, theta_0: float, l: float) -> tuple[np.ndarray, np.ndarray]:
    theta = np.full_like(t_vals, np.deg2rad(theta_0))
    omega = np.zeros_like(t_vals)
    dt = t_vals[1]-t_vals[0]

    for t_i in range(len(t_vals) - 1):
        omega[t_i] = omega[t_i-1] - (9.8/l)*np.sin(theta[t_i-1])*dt
        theta[t_i] = theta[t_i-1]+omega[t_i]*dt

    return theta


def linear_pendulum_analytic(t_vals: np.ndarray, theta_0: float, w: float):
    theta = theta_0*np.sin(w*t_vals)
    return theta


t_v = np.arange(0, 10, 0.01)
pyplot.plot(t_v, euler_chromer1(t_v, 80, 1), label=r"$\theta=10$")
pyplot.plot(t_v, euler_chromer(t_v, 80, 1), label=r"-$\theta=80$")
# pyplot.plot(t_v, linear_pendulum_analytic(t_v, 10, np.sqrt(9.8)), label=r"an$\theta=10$")
# pyplot.plot(t_v, linear_pendulum_analytic(t_v, 80, np.sqrt(9.8)), label=r"an$\theta=80$")
pyplot.legend()
pyplot.show()
