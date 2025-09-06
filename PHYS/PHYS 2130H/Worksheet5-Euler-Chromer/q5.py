import numpy as np
import matplotlib.pyplot as pyplot

def euler(t_vals: np.ndarray, h_0: float, v_0: float) -> tuple[np.ndarray, np.ndarray]:
    v_y = np.ndarray((t_vals.shape))
    y = np.ndarray((t_vals.shape))

    v_y[0] = v_0
    y[0] = h_0

    for t_i in range(len(t_vals) - 1):
        v_y[t_i+1] = v_y[t_i] - 9.8*(t_vals[1]-t_vals[0])
        y[t_i+1] = y[t_i] + v_y[t_i]*(t_vals[1]-t_vals[0])

    return (y, v_y)

def euler_chromer(t_vals: np.ndarray, h_0: float, v_0: float) -> tuple[np.ndarray, np.ndarray]:
    v_y = np.ndarray((t_vals.shape))
    y = np.ndarray((t_vals.shape))

    v_y[0] = v_0
    y[0] = h_0

    for t_i in range(len(t_vals) - 1):
        v_y[t_i+1] = v_y[t_i] - 9.8*(t_vals[1]-t_vals[0])
        y[t_i+1] = y[t_i] + v_y[t_i+1]*(t_vals[1]-t_vals[0])

    return (y, v_y)

t_v = np.arange(0, 3, 0.1)

y, v_y = euler(t_v, 3, 1)
y_c, v_y_c = euler_chromer(t_v, 3, 1)

pyplot.plot(t_v, y, label="y")
pyplot.plot(t_v, v_y, label="v_y")
pyplot.legend()

pyplot.figure()
pyplot.plot(t_v, y_c, label="y_c")
pyplot.plot(t_v, v_y_c, label="v_y_c")
pyplot.legend()

pyplot.show()