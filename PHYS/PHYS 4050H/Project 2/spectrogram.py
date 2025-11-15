import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal
from scipy.io import wavfile
import matplotlib
font = {'size'   : 22}

matplotlib.rc('font', **font)

fpath = "PHYS/PHYS 4050H/Project 2/audio/harmonics.wav"
sample_rate, samples = wavfile.read(fpath)

shap = samples.shape[0]
trimmed = samples[int(shap // 2 - shap // 4):int(shap // 2 + shap // 4)]

frequencies, times, spectrogram = signal.spectrogram(
    trimmed, sample_rate, nperseg=2048)

pcm = plt.pcolormesh(times, frequencies, np.log(spectrogram))
colours = ["red", "white", "orange", "pink", "black", "brown"]
for i in range(1, 7):
    ty = np.arange(10, (8.6 * 10**3) * i, i)
    x = np.linspace(start=5, stop=13.5, num=len(ty))
    plt.plot(x, ty, label=f"Harmonic {i-1}", linestyle='--', color=colours[i-1])

plt.ylim([0,22040])
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.title(os.path.splitext(os.path.basename(fpath))[0])
cbar = plt.colorbar(pcm)
cbar.set_label("log intensity")
plt.legend()
plt.show()
