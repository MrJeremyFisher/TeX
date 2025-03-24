import numpy as np
import seaborn as sns
import scipy.special as sp
from matplotlib import pyplot as pyplot
from scipy.constants import physical_constants


def plot_density(n, l, m_l, scaling_factor, phi):
    # TODO: quantum number constraints

    fig, ax = pyplot.subplots(figsize=(16, 16.5))

    grid_extent = 480
    grid_resolution = 1000
    x = y = np.linspace(-grid_extent, grid_extent, grid_resolution)
    x, y = np.meshgrid(x, y)

    eps = np.finfo(float).eps
    # 1 / (2 * (n + l + m_l))
    a_0 = scaling_factor * \
        physical_constants['Bohr radius'][0] * 1e+12

    radial_wfn = calculate_radial_wfn(n, l, np.sqrt((x ** 2 + y ** 2)), a_0)
    # Ignore phi because we are looking at a slice
    angular_wfn = calculate_angular_wfn(l, m_l, np.arctan(x / (y)), phi)

    psi = radial_wfn * angular_wfn
    prob_density = np.abs(psi)**2
    im = ax.imshow(np.sqrt(prob_density),
                   cmap=sns.color_palette('mako', as_cmap=True))
    pyplot.colorbar(im)
    pyplot.show()


def calculate_radial_wfn(n, l, r, a_0):
    norm = np.sqrt(
        ((2 / n * a_0) ** 3 * (sp.factorial(n - l - 1))) /
        (2 * n * (sp.factorial(n + l)))
    )
    laguerre_polynomial = sp.genlaguerre(n - l - 1, 2 * l + 1)

    rho = 2 * r / (n * a_0)

    return norm * np.exp(- rho / 2) * (rho ** l) * laguerre_polynomial(rho)


def calculate_angular_wfn(l, m_l, theta, phi):
    # Order (int or float). If passed a float not equal to an integer the function returns NaN.
    # Degree (float).
    # Argument (float). Must have |x| <= 1
    norm = ((-1) ** m_l) * np.sqrt(
        ((2 * l + 1) * sp.factorial(l - np.abs(m_l))) /
        (4 * np.pi * sp.factorial(l + np.abs(m_l)))
    )
    legendre_polynomial = sp.lpmv(m_l, l, np.cos(theta))

    return norm * legendre_polynomial * np.exp(1.j * m_l * phi)


plot_density(3, 2, 2, 0.4, 0)
