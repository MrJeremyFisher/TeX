import matplotlib.pyplot as pyplot
import numpy as np
from math import sin, pi

SAMPLES = 16
FREQUENCY = 1000
PERIOD = 1e6 / (FREQUENCY * SAMPLES)
next = 0

phase = 0
now = 0
SIN_LUT = [0]*SAMPLES

v = []
v_amp = []

for k in range(SAMPLES):
    SIN_LUT[k] = ((320000 / 2) * (sin(2 * pi * k / SAMPLES) + 1))

rng = np.arange(100)
for t in rng:
  now = now + 100

  if (now > next):
    command = 0x3000
    command |= (int(SIN_LUT[phase]) & 0x0FFF)

    v_amp.append(int(SIN_LUT[phase]) & 0x0FFF)
    v.append(int(SIN_LUT[phase]))

    phase = (phase + 1) % SAMPLES
    next += PERIOD

pyplot.step(rng, v, label="v")
pyplot.step(rng, v, label="AND")
pyplot.legend()
pyplot.show()