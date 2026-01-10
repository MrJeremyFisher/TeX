import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib
import os

font = {'size': 22}
matplotlib.rc('font', **font)
matplotlib.rcParams["savefig.directory"] = os.chdir(os.path.dirname(__file__))

A = 1
resolution = 500
zb = 5
# levels = np.linspace(-1, 1, 300)


def Vf(a, z, u):
    return sum([((z / np.abs(z)) * (2 * a**(l + 1) / ((l + 1) * z**(l + 1)))) for l in range(1, u+1, 2)])


z = np.linspace(A, zb, resolution)
V = Vf(A, z, 7)
pyplot.plot(z, V, color="blue")

z = np.linspace(-zb, -A, resolution)
V = Vf(A, z, 7)
pyplot.plot(z, V, color="blue", label="potential")

lv = np.linspace(-Vf(A, A, 7), Vf(A, A, 7), resolution)
pyplot.plot(np.full_like(z, -A), lv, linestyle="dashed",
            color="black", label="bounds")
pyplot.plot(np.full_like(z, A), lv, linestyle="dashed", color="black")
pyplot.xlabel("z")
pyplot.ylabel("Pseudo-potential")
pyplot.title("Degree-7 Potential Approximation")
pyplot.legend()
pyplot.show()
