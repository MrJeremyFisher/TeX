import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import cm

# Recall our template was
# A0  .. X0
# . .     .
# .    .  .
# A25 .. X25
data = np.genfromtxt(
    "PHYS/PHYS 3200Y/Lab 1/EM heatmap data.csv", delimiter=",")
nums = data[:, 1]

x = np.linspace(0, 25, 26)
y = np.linspace(0, 25, 26)
xv, yv = np.meshgrid(x, y)

full_dat = np.zeros(shape=(26, 26))

# L
full_dat[12, 0:24] = np.concatenate(
    (nums[0:12], np.flip(nums[0:12])))

# K
full_dat[11, 0:24] = np.concatenate(
    (nums[12:24], np.flip(nums[12:24])))

# J
full_dat[10, 1:23] = np.concatenate(
    (nums[24:35], np.flip(nums[24:35])))

# I
full_dat[9, 1:23] = np.concatenate(
    (nums[35:46], np.flip(nums[35:46])))

# H
full_dat[8, 1:23] = np.concatenate(
    (nums[46:57], np.flip(nums[46:57])))

# G
full_dat[7, 2:22] = np.concatenate(
    (nums[57:67], np.flip(nums[57:67])))

# F
full_dat[6, 2:22] = np.concatenate(
    (nums[67:77], np.flip(nums[67:77])))

# E
full_dat[5, 3:21] = np.concatenate(
    (nums[77:86], np.flip(nums[77:86])))

# D
full_dat[4, 4:20] = np.concatenate(
    (nums[86:94], np.flip(nums[86:94])))

# C
full_dat[3, 5:19] = np.concatenate(
    (nums[94:101], np.flip(nums[94:101])))

# B
full_dat[2, 6:18] = np.concatenate(
    (nums[101:107], np.flip(nums[101:107])))

# A
full_dat[1, 8:16] = np.concatenate(
    (nums[107:111], np.flip(nums[107:111])))

full_dat = full_dat + np.flip(full_dat, axis=0)

ax = pyplot.figure().add_subplot(projection='3d')
ax.set_zlabel(r"$V_{probe}$ (mV)")

p = ax.plot_surface(xv, yv, full_dat, cmap=cm.coolwarm)
pyplot.colorbar(p)
pyplot.savefig("PHYS/PHYS 3200Y/Lab 1/hplot.png")
ax.view_init(elev=0, azim=0)
pyplot.savefig("PHYS/PHYS 3200Y/Lab 1/hplot-sideon.png")
ax.view_init(elev=90, azim=0)
pyplot.savefig("PHYS/PHYS 3200Y/Lab 1/hplot-topdown.png")

pyplot.show()
