from matplotlib import pyplot
import numpy as np


def plot_cal_norm(filename: str, plot=False, save_image=False, save_data=False) -> None:
    data = np.loadtxt(filename, delimiter=",")  # Load data from file
    lam = data[:, 0]  # Slice file array into x and y
    intens = data[:, 1]

    # Calibrate. Subtract min zon-zero value
    intens = intens - \
        np.min(np.ma.masked_array(intens, mask=intens == 0).min())
    # Normalize. Divide by greatest value so everything is scaled the same
    intens = intens / intens.max()
    if (plot):
        pyplot.plot(lam, intens)  # Plot with y log x lin
        pyplot.xlabel(r"Wavelength (nm)")
        pyplot.ylabel(r"Intensity (arbitrary)")
        if (save_image):
            pyplot.savefig(filename.removesuffix(".csv") + ".png")
    if (save_data):
        out = np.ndarray(data.shape)
        out[:, 0] = lam
        out[:, 1] = intens
        np.savetxt(filename.removesuffix(".csv") + "-PROCESSED" +
                   ".csv", out, delimiter=",", fmt='%f')
    pyplot.title(f"SNR: {10*np.log10(signaltonoise(intens))}")
    pyplot.show()


def signaltonoise(a, axis=0, ddof=0):
    # Borrowed from scipy v<1.0.0
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)


plot_cal_norm(
    "PHYS 2610H/Lab 3/Psi/Psi_VIS_100_1nm_250um_350-750.csv", plot=True)
