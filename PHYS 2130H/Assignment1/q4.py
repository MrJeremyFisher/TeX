import matplotlib.pyplot as pyplot
import numpy as np

max_time = 80
theta = 45 * (np.pi/180)
g = 9.81
mu = 0.5
k = 0.6
m = 10

print(g*np.sin(theta))
t = np.arange(0,max_time,0.01)

N = g*np.cos(theta)

def v_y(t):
    return 0*t

def v_x(t):
    return (-1/k)*((g*np.sin(theta)-mu*N)*np.e**(-k*t)+mu*N-g*np.sin(theta))

pyplot.plot(t, v_x(t))
pyplot.xlabel("Time (s)")
pyplot.ylabel("Velocity (m/s)")
pyplot.show()