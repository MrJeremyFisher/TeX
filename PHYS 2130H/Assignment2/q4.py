import numpy as np
import matplotlib.pyplot as pyplot
import math

U0 = 2
a = 5
x = np.arange(-10, 10, 0.01)
x_t = np.arange(-1, 1, 0.01)

mins = []
def F(x):
    return ((4*U0)/(a))*((x/a)**3-(x/a))

for x_val in x:
    if (math.isclose(F(x_val), 0, abs_tol = 1e-9)): # Hacky but works
        mins.append(x_val)

def U(x):
    return U0*(2*(x/a)**2-(x/a)**4)

def U_t(x):
    return (2*U0*x**2)/(a**2)

print(f"Points of equilibrium {np.ceil(mins)}") # Floating point approx needs to be rounded

pyplot.plot(x, U(x), label="U")
pyplot.plot(x_t, U_t(x_t), label="U_t")
pyplot.legend()
pyplot.xlabel("Position (m)")
pyplot.ylabel("Potential Energy (J)")
pyplot.show()
