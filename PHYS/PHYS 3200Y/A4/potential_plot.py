import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib
import os

font = {'size': 22}
matplotlib.rc('font', **font)
matplotlib.rcParams["savefig.directory"] = os.chdir(os.path.dirname(__file__))

E_0 = 1
a = 1
resolution = 500

x = np.linspace(-5,5,resolution)
y = np.linspace(-5,5,resolution)
X, Y = np.meshgrid(x, y)
Z = E_0 * (-(np.sqrt(X**2 + Y**2)) + a**2 /
           np.sqrt(X**2 + Y**2)) * np.cos(np.arctan(Y / X))

levels = np.linspace(-15, 0, 300)
pyplot.contourf(X, Y, Z, levels=levels, cmap="jet")
phi =  np.linspace(0, 2 * np.pi, 20)
pyplot.plot(a*np.cos(phi),a*np.sin(phi), color="black", linestyle="dashed")
pyplot.axis("equal")
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.colorbar()
pyplot.show()
