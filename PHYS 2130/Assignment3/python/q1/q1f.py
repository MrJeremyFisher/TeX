import numpy as np
import matplotlib.pyplot as pyplot
import q1b


t_vals = np.arange(0, 200, 0.1)


def harm_osc_damp_drive():
    t = np.arange(0, 100, 0.1)
    w_0 = 2
    beta = 0.25
    A = 1 
    w = 0.1 
    x_0 = 3
    w_1, B, phi, D, delta = q1b.harm_osc_params(w_0,
                                                beta,
                                                A,
                                                w,
                                                x_0)

    s = np.cos(w_1*t-phi)
    gamma = B*np.e**(-beta*t)
    x_c = s*gamma
    x_p = D*np.cos(w*t-delta)

    pyplot.plot(t, s, label=r"$s(t)$")
    pyplot.plot(t, gamma, label=r"$\Gamma(t)$")
    pyplot.plot(t, x_c, label=r"$x_c(t)$")
    pyplot.plot(t, x_p, label=r"$x_p(t)$")
    
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("Position (m)")
    pyplot.legend()
    pyplot.show()
    
harm_osc_damp_drive()



