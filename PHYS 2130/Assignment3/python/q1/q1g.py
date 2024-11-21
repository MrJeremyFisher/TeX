import numpy as np
import matplotlib.pyplot as pyplot
import q1c


def harm_osc_euler_cromer(w_0: float,
                          beta: float,
                          A: float,
                          w: float,
                          x_0: float,
                          t: np.ndarray
                          ):
    dt = t[1]-t[0]
    x = np.full_like(t, x_0)
    x_r = q1c.harm_osc_x_pos(w_0, beta, A, w, x_0, t)
    v = np.zeros_like(t)
    for t_i in range(len(t) - 1):
        a = A*np.cos(w*t[t_i])-2*beta*v[t_i]-w_0**2*x[t_i] # Should depend on position, right?


        v[t_i+1] = v[t_i] + a*dt
        x[t_i+1] = x[t_i] + v[t_i+1]*dt

    pyplot.plot(t, x, label="Numerical solution")
    pyplot.plot(t, x_r, label="Analytical solution")
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("Position (m)")
    pyplot.legend()
    pyplot.show()


t_vals = np.arange(0, 200, 0.01)
harm_osc_euler_cromer(2, 0.25, 1, 0.1, 3, t_vals)
