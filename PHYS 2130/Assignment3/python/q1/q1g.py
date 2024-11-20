import numpy as np

def harm_osc_euler_cromer(w_0: float,
                   beta: float,
                   A: float,
                   w: float,
                   x_0: float,
                   t: np.ndarray
                   ) -> list:
    x = np.full_like(x_0)
    
    for t_i in range(len(t) - 1):
        

    return B*np.exp(-beta*t)*np.cos(w_1*t-phi)+D*np.cos(w*t-delta)
