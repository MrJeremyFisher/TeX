import matplotlib.pyplot as pyplot
import numpy as np

m = 10
theta = 30
k = 100
x0 = 0.3
g = 9.8

x_range = np.arange(0,5,0.01)

def U(x):
    return -1*m*g*(x-x0)*np.sin(np.deg2rad(theta))+(1/2)*k*(x-x0)**2

vals = [0]*len(x_range)
for val in range(len(x_range)):
    vals[val] = U(x_range[val])

pyplot.plot(x_range, vals)
pyplot.show()