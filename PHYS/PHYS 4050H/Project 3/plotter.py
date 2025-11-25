import matplotlib.pyplot as pyplot
import numpy as np
import matplotlib

font = {'size'   : 22}
matplotlib.rc('font', **font)


data = np.genfromtxt("PHYS/PHYS 4050H/Project 3/largepanel.csv", delimiter=",")
fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:, 1], data[:, 0], label="I(V)", color="blue")
ax.set_ylabel("Current (mA)")
ax.set_xlabel("Voltage (V)")


ax1 = ax.twinx()
ax1.scatter(data[:, 1], (data[:, 0] / 1000) * data[:, 1] *
            1000, label="P(V)", color="red")
ax1.set_ylabel("Power (mW)")

pyplot.show()
