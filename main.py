import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

# == initializing the variables to use
ECG = []

# == the part of the signal before P
x = np.linspace(0, 3.1416, 100)
for i in range(10):
    ECG.append(0)

# == drwing the P part
x = np.linspace(0, 3.1416, 11)
for i in range(len(x)):
    sin = 1.5 * np.sin(x[i])
    ECG.append(sin)

# == drawing the PR segment
for i in range(10):
    ECG.append(0)

# == drawing the QRS complex
x = np.linspace(0, 3.1416, 12)
for i in range(len(x)):
    sin = 12 * np.sin(x[i])
    ECG.append(sin)

# == drawing ST segment
for i in range(10):
    ECG.append(0)

# == drawing T
x = np.linspace(0, 3.1416, 27)
for i in range(len(x)):
    sin = 2 * np.sin(x[i])
    ECG.append(sin)

for i in range(10):
    ECG.append(0)


# == applying the FFT

N = len(ECG)
yf = fft(ECG)
xf = fftfreq(N, 512)

# == plotting the results

fig, axs = plt.subplots(2,1)
axs[0].plot(ECG)
axs[0].set_xlabel('Frequence')
axs[0].set_ylabel('Time')
axs[0].grid(True)

axs[1].plot(xf, np.abs(yf))
axs[1].set_xlabel('Frequence')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)

plt.show()

