import numpy as np
from scipy.constants import epsilon_0
from scipy.signal import find_peaks, peak_widths
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt
import matplotlib

font = {"weight": "bold", "size": 22}
matplotlib.rc("font", **font)
plt.xscale("log")
odds = [1, 3, 5, 7]

for dir in ["0.17"]:
    n = 0
    m = 0
    for i in range(1, 14):
        data = np.loadtxt(
            f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab2c/Real Data/{dir}cm/SDS000{i:02d}.csv",
            skiprows=12,
            delimiter=",",
        )
        # freqs go as n*10^m, m increases every 4
        expected_frequency = odds[n] * 10**m
        if i % 4 == 0:
            m = m + 1
        if (n + 1) % 4 == 0:
            n = -1
        n = n + 1
        # print(expected_frequency)

        t = data[:, 0]
        VR = data[:, 1]
        V = data[:, 2]

        a_r = np.fft.rfft(VR)
        a_r = a_r[:128]
        a = np.fft.rfft(V)
        a = a[:128]
        nf = a.size

        dt = t[1] - t[0]
        N = len(t)

        f = np.arange(nf) / (N * dt)
        peaks, _ = find_peaks(np.abs(a_r), height=10)

        results_half = peak_widths(np.abs(a_r), peaks, rel_height=0.08)

        recovered_freq = f[np.argmax(np.abs(a_r))]

        print(f"{round(recovered_freq, 2)} & {round(results_half[0][0], 2)}\\\\")
        # print(round(results_half[0][0], 2), end=", ")
        plt.hlines(*results_half[1:], color="black")

        plt.plot(
            f,
            np.abs(a),
            label=f"Recov:{round(recovered_freq, 2)} Exp:{expected_frequency}",
        )


# plt.yscale("log")
plt.legend()
plt.show()
