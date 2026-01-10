import matplotlib.pyplot as pyplot
import numpy as np
import matplotlib
import os 
import itertools
font = {'size': 22}
matplotlib.rc('font', **font)

directory = "PHYS/PHYS 4050H/Project 3/data/"
    

marker = itertools.cycle((',', '+', '.', 'o', '*', '^', 'v', '>', '<')) 
for fname in os.listdir(directory):
    print(fname)
    data = np.genfromtxt(directory + fname, delimiter=",")
    title = fname.replace(".csv", "")
    xo = np.flip(data[:, 1])
    yo = np.flip(data[:, 0])
    x = [xo[0]]
    y = [yo[0]]
    for i, xv in enumerate(xo): # Filter non-increasing data
        if xv > x[-1]:
            x.append(xv)
            y.append(yo[i])
    pyplot.figure(0)
    pyplot.plot(x, y, label=f"I(V) ({int(title)/100}mm)" , marker=next(marker), markersize=12)
    pyplot.ylabel("Current (mA)")
    pyplot.xlabel("Voltage (V)")
    pyplot.legend(loc=1)

    pyplot.figure(1)
    pyplot.plot(x, np.array(x)*np.array(y), label=f"P(V) ({int(title)/100}mm)", marker=next(marker), markersize=12)
    pyplot.ylabel("Power (mW)")
    pyplot.xlabel("Voltage (V)")
    pyplot.legend()
pyplot.show()
