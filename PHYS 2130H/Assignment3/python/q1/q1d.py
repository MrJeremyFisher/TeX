import matplotlib.pyplot as pyplot
import numpy as np
import q1c


def harm_osc_x_plot_single(x: np.ndarray, t: np.ndarray) -> None:
    pyplot.plot(t, x)
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("Position (m)")
    pyplot.show()


t_vals = np.arange(0, 200, 0.1)
x_vals = q1c.harm_osc_x_pos(2, 0.25, 1, 0.1, 3, t_vals)
harm_osc_x_plot_single(x_vals, t_vals)
