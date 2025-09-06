import matplotlib.pyplot as pyplot
import numpy as np
from scipy.optimize import curve_fit
def plot_fitted_and_raw(data_path: str, 
                        mintime: float, 
                        maxtime: float,
                        guessed_values: tuple[float, float, float, float, float],
                        fig: int,
                        label: str = "",
                        display_hand_fit: bool = False):
    data = np.loadtxt(data_path, delimiter=",", skiprows=1)
    data = data[
    (data[:, 0] > mintime) &
    (data[:, 0] < maxtime)
    ]
    t_vals = data[:, 0]
    positions = data[:, 1]

    pyplot.figure(fig)

    pyplot.scatter(t_vals, positions, color = "green", label=label)

    x_0 = guessed_values[0]
    A = guessed_values[1]
    B = guessed_values[2]
    w_1 = guessed_values[3]
    d = guessed_values[4]

    def plot_fit(t, x, amp, beta, omega, delta):
        pos_vals = []
        for t_val in t:
            pos_vals.append(x + amp*(np.e**(-beta*t_val))*np.cos(omega*t_val-delta))
        return pos_vals
    
    if (display_hand_fit):
        p = plot_fit(t_vals, x_0, A, B, w_1, d)
        pyplot.plot(t_vals, p, label=f"{label}-hand-fit", color="red")
    popt, covm = curve_fit(plot_fit, t_vals, positions)
    pyplot.plot(t_vals, plot_fit(t_vals, *popt), label=f"{label}-machine-fit", color="red")
    pyplot.legend()
    pyplot.xlabel("time (s)")
    pyplot.ylabel("position (m)")
    return popt, covm

x_0 = 0.71
A = 0.177
B = 0.05
w_1 = 2.7
d = 1.3
guessed_fits = (x_0, A, B, w_1, d)
popt1, covm1 = plot_fitted_and_raw("./data/run1.csv", 0.55, 35, guessed_fits, 0, "run 1")
print(popt1)
for el in np.diag(covm1):
    print(np.sqrt(el))

x_0 = 0.6606
A = 0.2
B = 0.05
w_1 = 2.6
d = 1.3
guessed_fits = (x_0, A, B, w_1, d)
popt2, covm2 = plot_fitted_and_raw("./data/run2.csv", 0.35, 14, guessed_fits, 1, "run 2")
print(popt2)
for el in np.diag(covm2):
    print(np.sqrt(el))

pyplot.show()
