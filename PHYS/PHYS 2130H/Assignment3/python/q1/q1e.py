import numpy as np
import matplotlib.pyplot as pyplot
import q1c


t_vals = np.arange(0, 200, 0.1)

for beta in [0.1, 0.2, 0.5]:
    x_vals = q1c.harm_osc_x_pos(1, beta, 1, 0.1, 3, t_vals)
    pyplot.plot(t_vals, x_vals, label=rf"$\beta={beta}$")

pyplot.xlabel("Time (s)")
pyplot.ylabel("Position (m)")
pyplot.legend()
pyplot.show()
