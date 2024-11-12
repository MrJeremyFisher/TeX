import matplotlib.pyplot as pyplot
import numpy as np

m = 1
v_0 = 600
h_0 = 500
theta = 60 * (np.pi/180)
g = 9.81
k_vals = [0, 0.02, 0.04, 0.06]

t = np.arange(0, 10, 0.01)

def x(t, k):
    return (v_0*np.cos(theta))*t if k == 0 else ((v_0*np.cos(theta))/k)*(1-np.e**(-k*t)) # k=0 is a special case where there is no drag so we use the plain kinematic equation

def y(t, k):
    return h_0 + (v_0*np.sin(theta))*t - (1/2)*g*t**2 if k == 0 else (1/k**2)*(g+k*v_0*np.sin(theta))*(1-np.e**(-k*t)) + h_0 - (g*t**2)/k

for k in k_vals:
    pyplot.plot(x(t, k), y(t, k), label=f"k={k}")

pyplot.legend()
pyplot.ylim(bottom=0, top=2000)
pyplot.xlabel("x (m)")
pyplot.ylabel("y (m)")
pyplot.show()