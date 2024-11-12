import numpy as np

r = np.array([0.1, 0.3, 0.7, 1.1])
A = np.array([0.14, 1.01, 6.54, 14.7])

pfit, covm = np.polyfit(r, A, 2, cov = True)
print(pfit)
print(np.diag(covm))