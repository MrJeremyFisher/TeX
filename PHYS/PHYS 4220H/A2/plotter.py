import matplotlib.pyplot as plt
import numpy as np

n_1 = 1.5
n_2 = 1.3


angles = np.linspace(0, np.pi / 2, 100)
refracted_angles = np.arcsin(n_1 * np.sin(angles) / n_2)


def t_p(a, ar):  # p is TM
    return 2 * n_1 * np.cos(a) / (n_2 * np.cos(a) + n_1 * np.cos(ar))


def r_p(a, ar):
    return (n_2 * np.cos(a) - n_1 * np.cos(ar)) / (n_2 * np.cos(a) + n_1 * np.cos(ar))


def T_p(a, ar):
    return (np.cos(ar) / np.cos(a)) * (n_2 / n_1) * t_p(a, ar)**2


def R_p(a, ar):
    return r_p(a, ar)**2


def t_s(a, ar):  # s is TE
    return 2 * n_1 * np.cos(a) / (n_1 * np.cos(a) + n_2 * np.cos(ar))


def r_s(a, ar):
    return (n_1 * np.cos(a) - n_2 * np.cos(ar)) / (n_1 * np.cos(a) + n_2 * np.cos(ar))


def T_s(a, ar):
    return (np.cos(ar) / np.cos(a)) * (n_2 / n_1) * t_s(a, ar)**2


def R_s(a, ar):
    return r_s(a, ar)**2

ang_deg = angles*180/np.pi

plt.figure(0)
plt.title("TM Incidence")
t_p_vals = np.nan_to_num(t_p(angles, refracted_angles), nan=0)
r_p_vals = np.nan_to_num(r_p(angles, refracted_angles), nan=1)
plt.plot(ang_deg, t_p_vals, label="t")
plt.plot(ang_deg, r_p_vals, label="r")

T_p_vals = np.nan_to_num(T_p(angles, refracted_angles), nan=0)
R_p_vals = np.nan_to_num(R_p(angles, refracted_angles), nan=1)
plt.plot(ang_deg, T_p_vals, label="T")
plt.plot(ang_deg, R_p_vals, label="R")
plt.legend()

plt.figure(2)
plt.title("TE Incidence")
t_s_vals = np.nan_to_num(t_s(angles, refracted_angles), nan=0)
r_s_vals = np.nan_to_num(r_s(angles, refracted_angles), nan=1)
plt.plot(ang_deg, t_s_vals, label="t")
plt.plot(ang_deg, r_s_vals, label="r")

T_s_vals = np.nan_to_num(T_s(angles, refracted_angles), nan=0)
R_s_vals = np.nan_to_num(R_s(angles, refracted_angles), nan=1)
plt.plot(ang_deg, T_s_vals, label="T")
plt.plot(ang_deg, R_s_vals, label="R")
plt.legend()
plt.show()
