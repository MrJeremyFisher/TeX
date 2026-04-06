import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import ode as ode
from matplotlib import cm
from itertools import product


class charge:
    def __init__(self, q, pos):
        self.q = q
        self.pos = pos


def E_point_charge(q, a, x, y):
    return q * (x - a[0]) / ((x - a[0])**2 + (y - a[1])**2)**(1.5), \
        q * (y - a[1]) / ((x - a[0])**2 + (y - a[1])**2)**(1.5)


def E_total(x, y, charges):
    Ex, Ey = 0, 0
    for C in charges:
        E = E_point_charge(C.q, C.pos, x, y)
        Ex = Ex + E[0]
        Ey = Ey + E[1]
    return [Ex, Ey]


def E_dir(t, y, charges):
    Ex, Ey = E_total(y[0], y[1], charges)
    n = np.sqrt(Ex**2 + Ey * Ey)
    return [Ex / n, Ey / n]


def V_point_charge(q, a, x, y):
    return q / ((x - a[0])**2 + (y - a[1])**2)**(0.5)


def V_total(x, y, charges):
    V = 0
    for C in charges:
        Vp = V_point_charge(C.q, C.pos, x, y)
        V = V + Vp
    return V


# calculate electric potential
x0, x1 = -3, 3
y0, y1 = -3, 3
R = 0.01
charges = [charge(-1, [-1, 1]), charge(1, [1, 1]),
           charge(-1, [1, -1]), charge(1, [-1, -1])]
vvs = []
xxs = []
yys = []
numcalcv = 300
for xx, yy in product(np.linspace(x0, x1, numcalcv), np.linspace(y0, y1, numcalcv)):
    xxs.append(xx)
    yys.append(yy)
    vvs.append(V_total(xx, yy, charges))
xxs = np.array(xxs)
yys = np.array(yys)
vvs = np.array(vvs)


# plot point charges
for C in charges:
    if C.q > 0:
        plt.plot(C.pos[0], C.pos[1], 'ro', ms=8 * np.sqrt(C.q))
    if C.q < 0:
        plt.plot(C.pos[0], C.pos[1], 'bo', ms=8 * np.sqrt(-C.q))

# plot electric potential
clim0, clim1 = -2, 2
vvs[np.where(vvs < clim0)] = clim0 * 0.999999  # to avoid error
vvs[np.where(vvs > clim1)] = clim1 * 0.999999  # to avoid error

plt.tricontourf(xxs, yys, vvs, 100, cmap=cm.jet)
cbar = plt.colorbar()
cbar.set_ticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
cbar.set_label("Electric Potential")
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
# plt.xlim(x0, x1)
# plt.ylim(y0, y1)
# plt.axes().set_aspect('equal', 'datalim')
plt.show()
