import numpy as np


def harm_osc_euler_cromer(w_0: float,
                          beta: float,
                          A: float,
                          w: float,
                          x_0: float,
                          t: np.ndarray
                          ) -> list:
    dt = t[1]-t[0]
    x = np.full_like(t, x_0)
    v = np.full_like(t, )
    for t_i in range(len(t) - 1):
        v[t_i+1] = v_y[t_i] - 9.8*(t_vals[1]-t_vals[0])
        y[t_i+1] = y[t_i] + v_y[t_i+1]*(t_vals[1]-t_vals[0])
    return B*np.exp(-beta*t)*np.cos(w_1*t-phi)+D*np.cos(w*t-delta)
