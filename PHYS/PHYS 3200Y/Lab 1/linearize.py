import numpy as np
import matplotlib.pyplot as pyplot

V_0 = 7.74
a = 0.0577
b = 0.2125

xax1 = np.arange(a, b, 0.01)
pyplot.plot(xax1, 
            1000*(V_0*np.log(xax1/b)/np.log(a/b)),
            label="Calculated", linestyle="--"
            )
pyplot.semilogx()
pyplot.legend()
pyplot.show()