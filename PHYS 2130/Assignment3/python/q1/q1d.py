import matplotlib.pyplot as pyplot
import numpy as np
from q1 import q1c

t_vals = np.arange(0, 1000, 0.1)
x_vals = q1c.harm_osc_x_pos(1, 0.01, 2, 0.1, 2, t_vals)


def harm_osc_x_plot_single(x: np.ndarray, t: np.ndarray) -> None:
    pyplot.plot(t, x)
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("Position (m)")
    pyplot.legend
    pyplot.show()
