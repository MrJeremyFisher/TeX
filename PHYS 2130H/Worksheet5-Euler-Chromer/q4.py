import numpy as np

def hyp(opp, adj):
    return np.sqrt(opp**2+adj**2)

print(hyp(3,4))