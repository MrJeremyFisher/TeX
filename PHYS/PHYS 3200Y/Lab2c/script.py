import numpy as np
import matplotlib.pyplot as plt


def f(x, A, nu):
    return A * np.cos(x * nu)


def fn(nf, T, A, nu):
    # define a function that generates the fourier transform of f in the
    # interval [-nf, nf] and for 0 < t < T
    wn = np.arange(-nf, nf + 1) * 2 * np.pi / T
    ftilde = np.where(np.abs(wn) > 1e-8,
                      (A / 2) * (((np.exp(1j * nu * T) - 1) / (1j * (nu - wn))
                                  ) + ((np.exp(-1j * nu * T) - 1) / (-1j * (nu + wn)))),
                      0)
    return wn, ftilde


T = 120
A = 1
nu = (3+0.0001) * np.pi
nf = 200
nt = 10000
t = np.linspace(0, T, nt)

# Plot the fourier transform:
f1 = plt.figure(1, clear=True)
ax1 = f1.add_subplot(111)
wn, ftilde = fn(nf, T, A, nu)
ax1.plot(wn, ftilde.real, marker='.', label='Re(fn)')
ax1.plot(wn, ftilde.imag, marker='.', label='Im(fn)')
# ax1.plot(wn, np.abs(ftilde), marker='.', label='abs(fn)')
ax1.legend()
ax1.set_xlim(-nf, nf)
ax1.set_ylabel(r'$\tilde f(\omega_n)$')
ax1.set_xlabel(r'$\omega_n$')


f0 = plt.figure(0, clear=True)
ax0 = f0.add_subplot(111)
# Plot the original function:
ax0.plot(t, f(t, A, nu), c='k', linestyle="dashed")
# Now use the Fourier transform to reconstruct the original function
for n in range(0, nf, 50):
    ft = np.zeros(nt, dtype=complex)
    for i in range(-n, n + 1):
        ft += ftilde[i + nf] * np.exp(1j * wn[i + nf] * t) / T

    ax0.plot(t, ft.real, label=r'$N_\mathrm{max} = %i$' % (n))

ax0.legend()
ax0.set_xlabel(r'$t$')
ax0.set_ylabel(r'$f(t)$')
plt.show()
