import matplotlib.pyplot as pyplot
import numpy as np

# I <3 avoiding code repetition
def plot_trimmed(path: str, label: str, mintime: float, minpos: float, maxtime: float) -> None:
    data = np.loadtxt(path, delimiter=",", skiprows=1) # does this path syntax work on windows? who knows
    data = data[ # not sure if there's a "smarter" way of doing this
        (data[:, 0] > mintime) & 
        (data[:, 1] > minpos) & 
        (data[:, 0] < maxtime)
    ]
    times = data[:, 0]
    positions = data[:, 1]
    pyplot.plot(times, positions, label=label)

plot_trimmed("./data/run1.csv", "run 1", .45, .1, 2.5)

plot_trimmed("./data/run2.csv", "run 2", .4, .1, 2.2)

plot_trimmed("./data/run3.csv", "run 3", 1, .1, 3)

pyplot.xlabel("Time (s)")
pyplot.ylabel("Position (m)")
pyplot.legend()
pyplot.show()