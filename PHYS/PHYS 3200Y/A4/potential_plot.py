import numpy as np
import matplotlib.pyplot as pyplot

E_0 = 1
a = 1
resolution = 500

x = np.linspace(-5,5,resolution)
y = np.linspace(-5,5,resolution)
X, Y = np.meshgrid(x, y)
Z = E_0 * (-(np.sqrt(X**2 + Y**2)) + a**2 /
           np.sqrt(X**2 + Y**2)) * np.cos(np.arctan(Y / X))

# E = np.gradient(Z)

levels = np.linspace(-15, 0, 300)
pyplot.contourf(X, Y, Z, levels=levels, cmap="jet")
phi =  np.linspace(0, 2 * np.pi, 20)
pyplot.plot(a*np.cos(phi),a*np.sin(phi), color="black", linestyle="dashed")

# step = 10
# s = max(np.max(E[0]), np.max(E[1])) * 0.1
# pyplot.quiver(X[::step,::step], Y[::step,::step], E[1][::step,::step], E[0][::step,::step], units='xy', pivot='tail', width=0.03, scale=1)
pyplot.axis("equal")
pyplot.colorbar()
pyplot.show()
