import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal
from scipy.io import wavfile

fpaths = ["PHYS/PHYS 4050H/Project 2/audio/raw_audio.wav",
"PHYS/PHYS 4050H/Project 2/audio/manufacturer_corrected.wav",
"PHYS/PHYS 4050H/Project 2/audio/diff.wav",
          ]

fig, axes = plt.subplots(1, 3, constrained_layout=True)
# fig.tight_layout()
for i, fpath in enumerate(fpaths):
    sample_rate, samples = wavfile.read(fpath)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    pcm = axes[i].pcolormesh(times, frequencies, np.log(spectrogram))
    axes[i].set_ylabel("Frequency (Hz)")
    axes[i].set_xlabel("Time s")
    axes[i].set_title(os.path.splitext(os.path.basename(fpath))[0])
cbar = fig.colorbar(pcm)
cbar.set_label("log intensity")
plt.show()