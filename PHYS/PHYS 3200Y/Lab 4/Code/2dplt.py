import numpy as np
import matplotlib.pyplot as plt

i = 5

data = np.genfromtxt(
    fname=f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}.csv", delimiter=",", skip_header=1)

ax_field = data[:, 1]
perp_field = data[:, 2]
position = data[:, 6]-0.083

plt.scatter(x=position,
            y=ax_field, label="axial field", color="orange")

plt.scatter(x=position,
            y=perp_field * 10000, label="perp field")


# np.savetxt(f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}-out.csv", np.stack((ax_field,
#                                                                                                    perp_field * 10000,
#                                                                                                    position), axis=-1), delimiter=",",
#            header=f"axial, perp, pos",
#            fmt="%.6g")

plt.xlabel("Position (m)")
plt.ylabel("Field (G)")
plt.legend()
plt.show()
