S1 = [1.9663, 1.9094, 1.66277, 1.84869]
S3 = [1.93347, 1.90298, 1.83241, 1.59856]
P1 = [1.93949, 1.91493, 1.86209, 1.71135]
P3 = [1.93808, 1.91217, 1.85564, 1.69087]
D1 = [1.93925, 1.91447, 1.86105]
D3 = [1.93925, 1.91444, 1.86102]


def levels(from_states, to_states):
    for f in range(len(from_states) - 1):
        for t in range(len(to_states)-1):
            from_state = from_states[f]
            to_state = to_states[t]
            if (from_state > to_state):
                dE = (from_state-to_state)
                wavelength = (100)/(dE)
                if (wavelength > 300 and wavelength < 790):
                    print(wavelength)

levels(P1, S1)
levels(D1, P1)
levels(P3, S3)
levels(D3, P3)