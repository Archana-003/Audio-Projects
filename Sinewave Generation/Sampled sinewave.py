import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
fs = 44100
f = 500
t = np.arange(0, 10, 1/fs)
x = 0.8 * np.sin(2*np.pi*f*t)
write("sine_500Hz.wav", fs, x.astype(np.float32))
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(X), 1/fs)
N = len(X)
plt.plot(freq[:N//2], np.abs(X[:N//2])/(N/2))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
