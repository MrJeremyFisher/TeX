import numpy as np
import matplotlib.pyplot as plt

i = 2

data = np.genfromtxt(
    fname=f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}.csv", delimiter=",", skip_header=1)

ax_field = data[:, 1]
perp_field = data[:, 2]
position = data[:, 6]

plt.scatter(x=position,
            y=ax_field, label="axial field")

plt.scatter(x=position,
            y=perp_field * 10000, label="perp field")

i = 3

data = np.genfromtxt(
    fname=f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}.csv", delimiter=",", skip_header=1)

ax_field1 = data[:, 1]
perp_field1 = data[:, 2]
position1 = data[:, 6]


plt.scatter(x=position1,
            y=ax_field1, label="axial field")

plt.scatter(x=position1,
            y=perp_field1 * 10000, label="perp field")


# plt.scatter(x=position1,
#             y=ax_field+ax_field1, label="sum")
# np.savetxt(f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}-out.csv", np.stack((ax_field,
#                                                                                                    perp_field * 10000,
#                                                                                                    position), axis=-1), delimiter=",",
#            header=f"axial, perp, pos",
#            fmt="%.6g")

plt.xlabel("Position (m)")
plt.ylabel("Field (G)")
plt.legend()
plt.show()
