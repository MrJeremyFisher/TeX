import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt("PHYS/PHYS 3200Y/Lab 2B/SDS00023.csv",
                  skiprows=2, delimiter=",")

t = data[:, 0]
V = data[:, 1]
V1 = data[:, 2]

a = np.fft.rfft(V)
nf = a.size

dt = t[1] - t[0]
N = len(t)
f = np.arange(nf) / (N * dt)
fig, axes = plt.subplots(1, 3)

axes[0].plot(f, a.real)
axes[0].set_title("real")
axes[1].plot(f, a.imag)
axes[1].set_title("imag")
axes[2].plot(f, np.abs(a))
axes[2].set_title("abs")

plt.setp(axes, xscale="log")
plt.figure(2)
plt.plot(t, V, label="proc")
plt.plot(t, V1, label="ref")
plt.title("Data")
plt.legend()
plt.show()
