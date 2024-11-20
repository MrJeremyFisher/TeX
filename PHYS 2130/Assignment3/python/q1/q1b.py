import numpy as np


def harm_osc_params(w_0: float,
                    beta: float,
                    A: float,
                    w: float,
                    x_0: float
                    ) -> tuple[float, float, float, float, float]:
    # "Given"
    w_1 = np.sqrt(w_0**2-beta**2)
    D = A/(np.sqrt((w_0**2-w**2)+4*(w**2)*beta**2))
    delta = np.atan((2*w*beta)/(w_0**2-w**2))

    # Unknowns
    phi = np.atan((beta-((D*w*np.sin(delta))/(x_0-D*np.cos(delta))))/w_1)
    B = (x_0-D*np.cos(delta))/(np.cos(phi))

    print(f"w_1: {w_1}", f"B: {B}", f"phi: {phi}",
          f"D: {D}", f"delta: {delta}", sep="\n")

    return w_1, B, phi, D, delta
