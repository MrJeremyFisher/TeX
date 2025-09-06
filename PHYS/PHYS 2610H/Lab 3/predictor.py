import pandas as pd

S1 = [1.9663, 1.9094, 1.66277, 1.84869]
S3 = [1.93347, 1.90298, 1.83241, 1.59856]
P1 = [1.93949, 1.91493, 1.86209, 1.71135]
P3 = [1.93808, 1.91217, 1.85564, 1.69087]
D1 = [1.93925, 1.91447, 1.86105]
D3 = [1.93925, 1.91444, 1.86102]

levels_list = dict()


def levels(E1, E2, E1n, E2n):
    for i in range(len(E1)):
        for j in range(len(E2)):
            dE = abs(E1[i]-E2[j])
            if dE > 0:
                wavelength = 1/dE*100
                if wavelength > 370 and wavelength < 750:
                    levels_list.update(
                        {"1s{}s{}-1s{}p{}".format(i, E1n, j, E2n): wavelength})


levels(S1, P1, "1S", "1P")
levels(P1, D1, "1P", "1D")
levels(S3, P3, "3S", "3P")
levels(P3, D3, "3P", "3D")
pd.DataFrame.from_dict(data=levels_list, orient="index").to_csv(
    "PHYS 2610H/Lab 3/predicted_vals.csv", header=False)
print(len(levels_list))
