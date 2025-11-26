import numpy as np
from matplotlib import pyplot as plt

freqs = []
caps = []
res = []

for i in range(1, 27):
    data = np.loadtxt(f"PHYS/PHYS 3200Y/Lab 2B/real data/SDS000{i:02d}.csv",
                      skiprows=12, delimiter=",")

    t = data[:, 0]
    V = data[:, 1]
    V1 = data[:, 2]

    a = np.fft.rfft(V)
    a1 = np.fft.rfft(V1)
    nf = a.size

    dt = t[1] - t[0]
    N = len(t)
    # plt.figure(i-1)
    f = np.arange(nf) / (N * dt)
    # fig, axes = plt.subplots(2, 3)

    # for i in range(0, 3):
    #     axes[0,i].set_xscale("log")

    # axes[0, 0].plot(f, a.real)
    # axes[0, 0].set_title("real")
    # axes[0, 1].plot(f, a.imag)
    # axes[0, 1].set_title("imag")
    # axes[0, 2].plot(f, np.abs(a))
    # axes[0, 2].set_title("abs")

    # axes[1, 0].plot(t, V, label="proc")
    # axes[1, 2].plot(t, V1, label="ref")

    index = np.argmax(np.abs(a))
    freqs.append(f[index])
    capacitance = (((a1/a)-1)*(0.22*10**-6))[index]
    caps.append(capacitance)
    resistance = (-2*np.pi*f[index]*np.imag(capacitance))**-1
    res.append(resistance)
    # fig.suptitle(f"{f[np.argmax(np.abs(a))]}Hz - {capacitance}F")
    # plt.legend()

fig, axes = plt.subplots(1, 3)
axes[0].plot(freqs, np.imag(caps))
axes[0].set_xscale("log")

axes[1].plot(freqs, np.real(caps))
axes[1].set_xscale("log")

axes[2].plot(freqs, res)
axes[2].set_xscale("log")
plt.show()
