import numpy as np
import matplotlib.pyplot as pyplot

g = 9.8
t = np.arange(0, 300, 0.1)


def euler_chromer_nonlinear(theta_0: float,
                            w_0: float,
                            l: float,
                            q: float,
                            F_d: float,
                            W: float,
                            t_vals: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    theta = np.full_like(t_vals, np.deg2rad(theta_0))
    omega = np.full_like(t_vals, w_0)
    dt = t_vals[1]-t_vals[0]
    for t_i in range(len(t_vals) - 1):
        omega[t_i+1] = omega[t_i] + \
            (-(g/l)*np.sin(theta[t_i])-q *
             omega[t_i] + F_d*np.sin(W*t_vals[t_i]))*dt
        theta[t_i+1] = theta[t_i]+omega[t_i+1]*dt

    return theta, omega


pyplot.figure(0)
pyplot.title(r"$F_D=0.5$")
theta_0, omega_0 = euler_chromer_nonlinear(10, 0, g, 0.5, 0.5, 2/3, t)

pyplot.plot(theta_0, omega_0, label=r"$\Delta\theta$")
pyplot.ylabel(r"$\omega \,(s^{-1})$")
pyplot.xlabel(r"$\theta\, \text{(rad)}$")
pyplot.legend()

pyplot.figure(1)
pyplot.title(r"$F_D=1.2$")
theta_0, omega_0 = euler_chromer_nonlinear(10, 0, g, 0.5, 1.2, 2/3, t)

pyplot.plot(theta_0, omega_0, label=r"$\Delta\theta$")
pyplot.ylabel(r"$\omega \,(s^{-1})$")
pyplot.xlabel(r"$\theta\, \text{(rad)}$")
pyplot.legend()

pyplot.show()