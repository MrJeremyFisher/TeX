import numpy as np
import matplotlib.pyplot as pyplot

v_0 = 3
h_0 = 1

g = 9.8

t_vals = np.arange(0, 3, 0.1)
v_y = np.ndarray((t_vals.shape))
y = np.ndarray((t_vals.shape))

v_y_c = np.ndarray((t_vals.shape))
y_c = np.ndarray((t_vals.shape))

v_y[0] = v_0
v_y_c[0] = v_0
y[0] = h_0
y_c[0] = h_0

a_v_y = np.ndarray((t_vals.shape))
a_y = np.ndarray((t_vals.shape))

for t_i in range(len(t_vals) - 1):
    v_y[t_i+1] = v_y[t_i] - g*(t_vals[1]-t_vals[0])
    y[t_i+1] = y[t_i] + v_y[t_i]*(t_vals[1]-t_vals[0])

    v_y_c[t_i+1] = v_y_c[t_i] -g*(t_vals[1]-t_vals[0])
    y_c[t_i+1] = y_c[t_i] + v_y_c[t_i+1]*(t_vals[1]-t_vals[0])

def y_a(t):
    return -(1/2)*g*t**2+v_0*t+h_0

def v_y_a(t):
    return -g*t+v_0

for t_i in range(len(t_vals)):
    a_v_y[t_i] = v_y_a(t_vals[t_i])
    a_y[t_i] = y_a(t_vals[t_i])



pyplot.plot(t_vals, a_v_y, label="real velocity", color="green")
pyplot.plot(t_vals, a_y, label="real y", color="red")

pyplot.scatter(t_vals, y, label="euler y", color="blue")
pyplot.scatter(t_vals, v_y, label="euler velocity", color="purple")
pyplot.legend()

pyplot.figure(2)
pyplot.plot(t_vals, a_v_y, label="real velocity", color="green")
pyplot.plot(t_vals, a_y, label="real y", color="red")

pyplot.scatter(t_vals, y_c, label="euler chroma y", color="orange")
pyplot.scatter(t_vals, v_y_c, label="euler chroma velocity", color="yellow")
pyplot.legend()

pyplot.figure(3)
pyplot.plot(t_vals, y-a_y, label="residual y")
pyplot.plot(t_vals, v_y-a_v_y, label="residual v_y")
pyplot.plot(t_vals, y_c-a_y, label="residual chroma y")
pyplot.plot(t_vals, v_y_c-a_v_y, label="residual chroma v_y")

pyplot.legend()
pyplot.show()