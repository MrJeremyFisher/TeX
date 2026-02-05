import numpy as np
from matplotlib import pyplot as plt

fig, axes = plt.subplots(1, 3)

k = 0
for i in (1,2,3):
    data = np.loadtxt(
        f"PHYS/PHYS 3200Y/Lab 2B/real data/SDS000{i:02d}.csv",
        skiprows=12,
        delimiter=",",
    )
    t = data[:, 0]
    V = data[:, 1]
    V1 = data[:, 2]

    a = np.fft.rfft(V1)
    nf = a.size

    dt = t[1] - t[0]
    N = len(t)
    f = np.arange(nf) / (N * dt)

    index = np.argmax(np.abs(a))

    
    axes[k].set_title(f"approx. {np.ceil(f[index])} Hz")
    axes[k].scatter(V, V1)
    k = k+1

axes[0].set_xlabel(r"$V$ (V)")
axes[0].set_ylabel(r"$V_r$ (V)")
plt.show()
