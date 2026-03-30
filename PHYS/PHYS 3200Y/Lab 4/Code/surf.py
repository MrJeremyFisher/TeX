import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
fig = go.Figure()
pos = np.array([1.5, 3, 5, 8]) * 10**-2


for i in range(6, 10):
    data = np.genfromtxt(
        fname=f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}.csv", delimiter=",", skip_header=1)

    ax_field = data[:, 1]
    perp_field = data[:, 2]
    position = data[:, 6]

    fakepos = np.full_like(position, pos[i - 6])
    dummy_stack = np.stack((ax_field,
                            perp_field * 10000,
                            fakepos,
                            position), axis=-1)

    # np.savetxt(f"/home/jeremy/Documents/TeX/PHYS/PHYS 3200Y/Lab 4/Code/Data/run{i}-out.csv", dummy_stack, delimiter=",",
    #            header=f"axial, perp, fakepos, pos",
    #            fmt="%.6g")

    # fig.add_trace(
    #     go.Scatter3d(
    #         x=position,
    #         y=fakepos,
    #         z=ax_field,
    #         marker=go.scatter3d.Marker(size=3),
    #         opacity=0.8,
    #         mode='markers'
    #     )
    # )

    # fig.add_trace(
    #     go.Scatter3d(
    #         x=position,
    #         y=fakepos,
    #         z=perp_field * 10000,
    #         marker=go.scatter3d.Marker(size=3),
    #         opacity=0.8,
    #         mode='markers'
    #     )
    # )


# fig.show()
plt.show()