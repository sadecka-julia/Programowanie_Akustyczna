import numpy as np
import pandas as pd
from scipy.fft import fft
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


class Generator:
    def __init__(self, sampling, time):
        self.sampling = sampling
        self.time = time
        self.t = np.linspace(0, self.time, self.time * self.sampling)

    def formula_sine(self, f, a):
        data = a * np.sin(2 * np.pi * f * self.t)
        return data

    def formula_square(self, f, a):
        data = a * np.sin(2 * np.pi * f * self.t)
        data = np.sign(data)
        return data

    def formula_sawtooth(self, f, a):
        data = a * 2 * (1 / np.pi) * np.arctan(np.tan(np.pi * f * self.t))  # + A * (np.random.rand(len(t)) - 0.5)
        return data

    def formula_triangle(self, f, a):
        data = a * 2 * (1 / np.pi) * np.arcsin(np.sin(2 * np.pi * f * self.t))  # + A * (np.random.rand(len(t)) - 0.5)
        return data

    def formula_white_noise(self, a):
        data = a * (np.random.rand(len(self.t)) - 0.5)
        return data

    def wykres(self, data):
        time_0 = float(input('Podaj początek zakresu: \n'))
        time = float(input('Podaj koniec zakresu: \n'))
        plt.plot(self.t, data, color='#88c999')
        plt.xlim(time_0, time)
        plt.show()

    def tranformata_fouriera(self, data):
        time_0 = float(input('Podaj początek zakresu: \n'))
        time = float(input('Podaj koniec zakresu: \n'))
        N = len(self.t)
        dt = self.t[1] - self.t[0]
        yf = 2.0 / N * np.abs(fft(data)[0:N // 2])
        xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
        plt.plot(xf, yf)
        plt.xlim(time_0, time)  # ogranicza wykres do zakresu od 0 do 1kHz
        plt.xlabel("frequency (Hz)")
        plt.ylabel("amplitude")
        plt.grid()
        plt.show()
        return xf, yf

    def save_data_to_file(self, data):
        name_of_file = input("Enter name of file: \n")
        xf, yf = Generator.tranformata_fouriera(self, data)
        data = {"freq": xf, "ampl": yf}
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(name_of_file, index=False, sep='\t')

    def save_audio_data(self, data):
        name_of_file = input("Enter name of file: \n")
        audio_data = np.int16(data * 2 ** 15)
        write(name_of_file, self.sampling, audio_data)


if __name__ == '__main__':
    flag1 = True
    while flag1 is True:
        sampling = int(input('Enter sampling: \n'))
        audio_time = int(input('Enter audio time: \n'))
        g = Generator(sampling, audio_time)

        flag2 = True
        while flag2 is True:
            try:
                kind = int(input('What formula do you want to make? '
                                 'Sine[1], Square[2], Sawtooth[3], Triangle[4], White Noise[5]:  \n'))
                if kind == 5:
                    a = float(input('Enter a: \n'))
                    y = Generator.formula_white_noise(g, a)
                else:
                    a = float(input('Enter a: \n'))
                    f = float(input('Enter f: \n'))
                    if kind == 1:
                        y = Generator.formula_sine(g, f, a)
                    elif kind == 2:
                        y = Generator.formula_square(g, f, a)
                    elif kind == 3:
                        y = Generator.formula_sawtooth(g, f, a)
                    elif kind == 4:
                        y = Generator.formula_triangle(g, f, a)
                    else:
                        raise ValueError

                flag3 = True
                while flag3 is True:
                    action = int(input('What you want to do with it?: figure[1], '
                                       'fourier transform[2], save data to file[3], save data to audio[4]: \n'))
                    if action == 1:
                        Generator.wykres(g, y)
                    elif action == 2:
                        Generator.tranformata_fouriera(g, y)
                    elif action == 3:
                        Generator.save_data_to_file(g, y)
                    elif action == 4:
                        Generator.save_audio_data(g, y)
                    else:
                        raise ValueError

                    ch_flag3 = input('Do you want do something else with this formula [y/n]: \n')
                    if ch_flag3 == 'n':
                        flag3 = False
            except:
                print('Wrong input. \n')
                continue

            ch_flag2 = input('Do you want another formula? [y/n]: \n')
            if ch_flag2 == 'n':
                flag2 = False

        ch_flag1 = input('Do you want do another generator? [y/n]: \n')
        if ch_flag1 == 'n':
            flag1 = False


