import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial # Used here over math.factorial as it can handle element-wise factorials of arrays


def Omega(N: int, X: int) -> int:
    return factorial(N) / (factorial(0.5 * (N + X)) * factorial(0.5 * (N - X)))


Ns = [4, 8, 16]
for N in Ns:
    X_vals = np.array([x for x in range(-N, N + 1, 2)])
    v = Omega(N, X_vals) / 2**N
    plt.plot(X_vals / N, v, label=f"N flips: {N}")

plt.xlabel("X/N")
plt.ylabel(r"$\Omega$")
plt.legend()
plt.show()
