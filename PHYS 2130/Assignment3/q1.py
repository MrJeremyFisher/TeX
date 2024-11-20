import numpy as np
import matplotlib.pyplot as pyplot


def harm_osc_params(w_0: float,
                    beta: float,
                    A: float,
                    w: float,
                    x_0: float
                    ) -> tuple[float, float, float, float, float]:
    # "Given"
    w_1 = np.sqrt(w_0**2-beta**2)
    D = A/(np.sqrt((w_0**2-w**2)+4*(w**2)*beta**2))
    delta = np.arctan((2*w*beta)/(w_0**2-w**2)) # Note: some versions of numpy use atan??

    # Unknowns
    phi = np.arctan((beta-((D*w*np.sin(delta))/(x_0-D*np.cos(delta))))/w_1)
    B = (x_0-D*np.cos(delta))/(np.cos(phi))

    print(f"w_1: {w_1}", f"B: {B}", f"phi: {phi}",
          f"D: {D}", f"delta: {delta}", sep="\n")

    return w_1, B, phi, D, delta


def harm_osc_x_pos(w_0: float,
                   beta: float,
                   A: float,
                   w: float,
                   x_0: float,
                   t: np.ndarray
                   ) -> list:
    w_1, B, phi, D, delta = harm_osc_params(w_0,
                                            beta,
                                            A,
                                            w,
                                            x_0)

    return B*np.exp(-beta*t)*np.cos(w_1*t-phi)+D*np.cos(w*t-delta)


def harm_osc_x_plot_single(x: np.ndarray, t: np.ndarray, fig: int) -> None:
    pyplot.plot(t, x)
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("Position (m)")
    pyplot.legend
    pyplot.show()


t_vals = np.arange(0, 1000, 0.1)
x_vals = harm_osc_x_pos(0.9, 0.01, 2, 0.1, 3, t_vals)
harm_osc_x_plot_single(x_vals, t_vals, 0)