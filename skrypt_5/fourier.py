from scipy.fft import fft
import matplotlib.pyplot as plt
import numpy as np


def wykres():
    sampling = 44100        # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5                # czas trwania wygenerowanego pliku
    A = 0.1                 # amplituda (od 0 do 1)
    f = 440                 # częstotliwość w Hz
    t = np.linspace(0, time, time*sampling)   # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania

    data = A*np.sin(2*np.pi*f*t)   # generuje przebieg


    def TranformataFouriera(t, y):
        N = len(t)
        dt = t[1] - t[0]
        yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
        xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
        return xf, yf


    xf, yf = TranformataFouriera(t, data)
    plt.plot(xf, yf)
    plt.xlim(0, 1000)   # ogranicza wykres do zakresu od 0 do 1kHz
    plt.xlabel("frequency (Hz)")
    plt.ylabel("amplitude")
    plt.grid()
    plt.show()


def prostokatny():
    sampling = 44100  # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5  # czas trwania wygenerowanego pliku
    A = 0.1  # amplituda (od 0 do 1)
    f = 440  # częstotliwość w Hz
    t = np.linspace(0, time, time * sampling)  # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania

    data = A * np.sin(2 * np.pi * f * t)        # generuje przebieg
    data = np.sign(data)


    def TranformataFouriera(t, y):
        N = len(t)
        dt = t[1] - t[0]
        yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
        xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
        return xf, yf

    xf, yf = TranformataFouriera(t, data)
    plt.plot(xf, yf)
    plt.xlim(0, 3000)  # ogranicza wykres do zakresu od 0 do 1kHz
    plt.xlabel("frequency (Hz)")
    plt.ylabel("amplitude")
    plt.grid()
    plt.show()


def szum():
    sampling = 44100   # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5           # czas trwania wygenerowanego pliku
    A = 1              # amplituda (od 0 do 1)
    f = 440  # częstotliwość w Hz
    t = np.linspace(0, time, time * sampling)  # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania

    data = A * np.sin(2 * np.pi * f * t) + A * (np.random.rand(len(t)) - 0.5) # generuje przebieg

    def TranformataFouriera(t, y):
        N = len(t)
        dt = t[1] - t[0]
        yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
        xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
        return xf, yf

    xf, yf = TranformataFouriera(t, data)
    plt.plot(xf, yf)
    plt.xlim(0, 3000)  # ogranicza wykres do zakresu od 0 do 1kHz
    plt.ylim(0, 0.005)
    plt.xlabel("frequency (Hz)")
    plt.ylabel("amplitude")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # szum()
    wykres()
    # prostokatny()
