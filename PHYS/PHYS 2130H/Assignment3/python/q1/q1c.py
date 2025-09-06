import numpy as np
import q1b


def harm_osc_x_pos(w_0: float,
                   beta: float,
                   A: float,
                   w: float,
                   x_0: float,
                   t: np.ndarray
                   ) -> list:
    w_1, B, phi, D, delta = q1b.harm_osc_params(w_0,
                                                beta,
                                                A,
                                                w,
                                                x_0)

    return B*np.exp(-beta*t)*np.cos(w_1*t-phi)+D*np.cos(w*t-delta)
