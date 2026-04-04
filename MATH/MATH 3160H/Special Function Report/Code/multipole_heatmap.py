import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


size = 500
extent = 0.003
xx, yy = np.meshgrid(np.linspace(-extent, extent, size), np.linspace(-extent, extent, size))


def dipole(x, y, q):
    return q*(1 / np.sqrt(x**2 + (y + 0.001)**2) - 1 / np.sqrt(x**2 + (y - 0.001)**2))

levels = np.linspace(-160000, 160000, 25)
plt.contour(dipole(xx, yy, 1), cmap='jet', levels=levels)
plt.colorbar()
plt.show()