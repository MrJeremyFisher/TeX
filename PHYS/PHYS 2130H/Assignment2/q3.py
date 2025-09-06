import numpy as np
import matplotlib.pyplot as pyplot

m = 1.5
k = 2
a = 0.7
t = np.arange(0, 5, 0.01)

def ac(t):
    return ((k*t)/m)*np.e**(-a*t)

def v(t):
    return -(k*t*np.e**(-a*t))/(m*a)-(np.e**(-a*t))/(a**2)*(k/m)+k/(a**2*m)

def x(t):
    return (k*t)/(a**2*m*np.e**(a*t))+(2*k)/(a**3*m*np.e**(a*t))+(k/(a**2*m))*t-((2*k)/(m*a**3))

pyplot.plot(t, ac(t), label="a")
pyplot.plot(t, v(t), label="v")
pyplot.plot(t, x(t), label="x")
pyplot.legend()
pyplot.xlabel("Time (s)")
pyplot.show()