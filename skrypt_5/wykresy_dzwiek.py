import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


def wykres():
    sampling = 44100       # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 10               # czas trwania wygenerowanego pliku
    A = 0.1                # amplituda (od 0 do 1)
    f = 440                # częstotliwość w Hz

    t = np.linspace(0, time, time*sampling)     # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania
    data = A*np.sin(2*np.pi*f*t)                # generuje przebieg
    audio_data = np.int16(data * 2**17)         # skaluje wygenerowany przebieg do przetwornika ADC 16 bit oraz rzutuje wygenerowany przebieg na typ całkowity int16

    write('test_sin.wav', sampling, audio_data)

    plt.plot(t, audio_data, color='#88c999')
    plt.xlim(0, 0.01)

    plt.show()


def sygnal_prostokatny():
    sampling = 44100       # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5               # czas trwania wygenerowanego pliku
    A = 0.1                # amplituda (od 0 do 1)
    f = 440                # częstotliwość w Hz

    t = np.linspace(0, time, time*sampling)     # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania
    data = A*np.sin(2*np.pi*f*t)                # generuje przebieg
    audio_data = np.int16(data * 2**15)
    audio_data = np.sign(audio_data)            # skaluje wygenerowany przebieg do przetwornika ADC 16 bit oraz rzutuje wygenerowany przebieg na typ całkowity int16

    write('test_kwadrat.wav', sampling, audio_data)

    plt.plot(t, audio_data, color='#88c999')
    plt.xlim(0, 0.01)

    plt.show()


def szum_bialy():
    sampling = 44100       # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5               # czas trwania wygenerowanego pliku
    A = float(input('Enter A: \n'))               # amplituda (od 0 do 1)
    f = 440                # częstotliwość w Hz

    t = np.linspace(0, time, time*sampling)     # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania
    data = A * (np.random.rand(len(t)) - 0.5)  # generuje przebieg
    audio_data = np.int16(data * 2**15)

    write('test_szum.wav', sampling, audio_data)

    plt.plot(t, audio_data, color='#88c999')
    plt.xlim(0, 0.01)

    plt.show()


def triangle():
    sampling = 44100       # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5              # czas trwania wygenerowanego pliku
    A = 0.1              # amplituda (od 0 do 1)
    f = 100               # częstotliwość w Hz

    t = np.linspace(0, time, time*sampling)     # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania
    data = A*2*(1/np.pi)*np.arcsin(np.sin(2*np.pi*f*t)) #+ A * (np.random.rand(len(t)) - 0.5)    # generuje przebieg
    audio_data = np.int16(data * 2**15)

    write('test_trojkat.wav', sampling, audio_data)

    plt.plot(t, audio_data, color='#88c999')
    plt.xlim(0, 0.1)

    plt.show()


def sawtooth():
    sampling = 44100       # częstotliwość próbkowania, https://en.wikipedia.org/wiki/44,100_Hz
    time = 5              # czas trwania wygenerowanego pliku
    A = 0.1              # amplituda (od 0 do 1)
    f = 100               # częstotliwość w Hz

    t = np.linspace(0, time, time*sampling)     # wektor czasu uwzględniający zadaną długość i częstotliwość próbkowania
    data = A*2*(1/np.pi)*np.arctan(np.tan(np.pi*f*t))# + A * (np.random.rand(len(t)) - 0.5)    # generuje przebieg
    audio_data = np.int16(data * 2**15)

    write('test_sawtooth.wav', sampling, audio_data)

    plt.plot(t, audio_data, color='#88c999')
    plt.xlim(0, 0.1)

    plt.show()


if __name__ == '__main__':
    wykres()
    sygnal_prostokatny()
    szum_bialy()
    triangle()
    sawtooth()
