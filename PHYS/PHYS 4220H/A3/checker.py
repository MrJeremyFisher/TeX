import numpy as np
from scipy.constants import c

a = 0.03
b = 0.01
arr = np.ndarray(shape=(10, 10), dtype=int)
for m in range(10):
    for n in range(10):
        arr[m, n] = 40.1 * 10**9 < c * np.sqrt((m / a)**2 + (n / b)**2) / 2
print(100-np.count_nonzero(arr))
