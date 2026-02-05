import numpy as np
from scipy.constants import epsilon_0
from matplotlib import pyplot as plt
import matplotlib

font = {"weight": "bold", "size": 22}
matplotlib.rc("font", **font)

k = 0
fig, axes = plt.subplots(1, 3)
axes[0].set_xscale("log")
axes[0].set_title("epsilon")

axes[1].set_xscale("log")
axes[1].set_title("abs(C) (F)")

axes[2].set_xscale("log")
axes[2].set_title("R")
for dir in ("0.17", "0.3", "0.49"):
    freqs = []
    caps = []
    res = []
    eps = []
    for i in range(1, 14):
        data = np.loadtxt(
            f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab2c/Real Data/{dir}cm/SDS000{i:02d}.csv",
            skiprows=12,
            delimiter=",",
        )
        t = data[:, 0]
        VR = data[:, 1]
        V = data[:, 2]

        a_r = np.fft.rfft(VR)
        a = np.fft.rfft(V)
        nf = a.size

        dt = t[1] - t[0]
        N = len(t)
        f = np.arange(nf) / (N * dt)

        index = np.argmax(np.abs(a))

        R = a[index] / a_r[index]
        phase = np.arctan2(np.imag(R), np.real(R))
        freqs.append(f[index])
        capacitance = ((0.22 * 10**-6) * (((a / a_r) * np.exp(1j * phase) - 1))**-1)[
            index
        ]
        caps.append(capacitance)  # C=eA/d => Cd/A=e
        eps.append((np.abs(capacitance) * float(dir)) / 0.064 / epsilon_0 / 100)
        resistance = (2 * np.pi * f[index] * np.imag(capacitance)) ** -1
        res.append(resistance)

    axes[0].plot(freqs, eps, label=dir)
    axes[1].plot(freqs, np.imag(caps), label=dir)
    axes[2].plot(freqs, res, label=dir)

    # out = np.stack(
    #     (
    #         freqs,
    #         np.abs(caps),
    #         res,
    #         eps
    #     ),
    #     axis=-1, dtype=np.float64
    # )

    # np.savetxt(
    #     f"PHYS/PHYS 3200Y/Lab2c/{dir}cm processed.csv",
    #     out,
    #     delimiter=",",
    #     header=f"freq (Hz), C_s (F), R, eps (/e_0)",
    #     fmt="%.6g",
    # )


plt.legend()
plt.show()
