import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Funkcja otwierająca i pobierająca dane z pliku podanego przez użytkownika
# Funkcja równocześnie sprawdza czy plik istnieje, jeśli nie prosi o ponowne podanie
def open_file():
        flag = True
        while flag is True:
            try:
                name = input("Enter name of file: \n")
                df = pd.read_csv(name, sep="\t")
                t = np.array(df['t'])
                a = np.array(df['a'])
                flag = False
            except FileNotFoundError:
                print('Wrong name of file. ')
                continue
        return t, a, name


# Funkcja malująca wykres z danych z pliku
def figure(t, a, name):
    x = np.array(t)
    y = np.array(a)

    plt.title(f'Wykres danych z pliku {name}')
    plt.xlabel('t')
    plt.ylabel('y')

    plt.scatter(x, y, color='#88c999')
    plt.show()


# Funkcja dopasowywująca parametry do wykresu funkcji
def adjustment(t, y):
    def func(x, A, f, gamma):
        return A * np.sin(2 * np.pi * f * x) * np.e ** ((-1) * gamma * x)

    p0 = [1, 1, 1]    # wektor inicjalizacji
    fit_params, covariance_matrix = curve_fit(func, t, y, p0=p0)   #fitowanie
    print("Parameter adjustment: \n a=", fit_params[0], "\n f=", fit_params[1], "\n y= ", fit_params[2])
    plt.scatter(t, y, color='#88c999')
    plt.plot(t, func(t, *fit_params), color='#EDF92E')
    plt.show()


if __name__ == '__main__':
    t, y, name = open_file()
    figure(t, y, name)
    confirm = input('Perform parameter adjustment? [t/n]')
    if confirm == 't':
        adjustment(t, y)




