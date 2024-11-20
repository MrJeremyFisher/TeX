import numpy as np

def euler(t_vals: np.ndarray, h_0: float, v_0: float, k: float, m: float) -> tuple[np.ndarray, np.ndarray]:
    v_y = np.ndarray((t_vals.shape))
    y = np.ndarray((t_vals.shape))

    v_y[0] = v_0
    y[0] = h_0

    for t_i in range(len(t_vals) - 1):
        v_y[t_i+1] = v_y[t_i] - 9.8*(t_vals[1]-t_vals[0])
        y[t_i+1] = y[t_i] + v_y[t_i]*(t_vals[1]-t_vals[0])

    return (y, v_y)