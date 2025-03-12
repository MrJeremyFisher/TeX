from matplotlib import pyplot
import numpy as np


def plot_cal_norm(filename: str, save = False) -> None:
    data = np.loadtxt(filename, delimiter=",") # Load data from file

    lam = data[:, 0] # Slice file array into x and y
    intens = data[:, 1]

    intens = intens - np.min(intens.nonzero()) # Calibrate. Subtract min zon-zero value
    intens = intens / intens.max() # Normalize. Divide by greatest value so everything is scaled the same

    pyplot.semilogy(lam, intens) # Plot with y log x lin
    pyplot.xlabel(r"Wavelength (nm)")
    pyplot.ylabel(r"Intensity (arbitrary)")
    
    if (save):
        pyplot.savefig(filename.removesuffix(".csv") + ".png")

    
    pyplot.show()
    
plot_cal_norm("PHYS 2610H/Lab 3/He/He_VIS_10_0.5nm_250um_350-500.csv")