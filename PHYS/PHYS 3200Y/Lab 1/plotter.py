import numpy as np
import matplotlib.pyplot as pyplot

V_0 = 7.76
a = 0.0577
b = 0.2125
dat_10 = [5450, 4110, 3020, 2140, 1420, 860]
dat_100 = [6180, 4550, 3300, 2250, 1430, 670]
dat_1000 = [5150, 3930, 3100, 2360, 1770, 1310]
yerrs = [250] * 6
xerrs = [0.002]*6
xax = np.linspace(a, b, 6)


def fun(x):
    return 1000 * (V_0 * np.log(x / b) / np.log(a / b))


pyplot.errorbar(xax, dat_10, yerr=yerrs, xerr=xerrs, label="10Hz", fmt="o")
pyplot.errorbar(xax, dat_100, yerr=yerrs, xerr=xerrs, label="100Hz", fmt="x")
pyplot.errorbar(xax, dat_1000, yerr=yerrs, xerr=xerrs, label="1000Hz", fmt="*")
pyplot.plot(xax, fun(xax),
            label="Calculated")
pyplot.ylabel(r"$V_{probe}$ (mV)")
pyplot.xlabel(r"(cm)")
pyplot.legend()
pyplot.savefig("PHYS/PHYS 3200Y/Lab 1/Figure_1.png")

pyplot.figure(2)
pyplot.plot(xax, abs(dat_10 - fun(xax)), label="10Hz Residual")
pyplot.plot(xax, abs(dat_100 - fun(xax)), label="100Hz Residual")
pyplot.plot(xax, abs(dat_1000 - fun(xax)), label="1000Hz Residual")

pyplot.legend()
pyplot.savefig("PHYS/PHYS 3200Y/Lab 1/Figure_2.png")
pyplot.show()
