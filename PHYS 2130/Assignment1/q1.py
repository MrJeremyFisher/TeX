import matplotlib.pyplot as pyplot
import numpy as np

t=np.arange(0,3,0.01)
def x(t):
    return -3*(1+t)*(np.log(1+t)-1) - 3
def y(t):
    return -(4/5)*np.cos(5*t) + 4/5

pyplot.plot(x(t),y(t))
pyplot.show()