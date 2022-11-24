import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Funkcja rysująca wykres z podanych wcześniej parametrów
def fading_sinusoid(A, a, f, gamma, t, t_step):
    x = np.linspace(0, t, num=t_step)      # dziedzina funkcji
    y = A * np.sin(2 * np.pi * f * x) * np.e ** ((-1) * gamma * x) + a * (np.random.rand(len(x)))    #zbiór wartości funkcji

    plt.scatter(x, y, color='#88c999')
    plt.title(f'y = {A}*sin(2*\u03C0*{f}*t)*e^(-{gamma}t)+{a}N(t)')
    plt.xlabel("Time[s]")
    plt.ylabel("y")
    plt.show()
    return x, y


# Funkcja pobierająca od użytkownika dane i sprawdzająca czy dane podane są w poprawnym formacie (float)
# Funkcja zwraca listę z danymi
def taking_data():
    tmp_list = ['A', 'a', 'f', 'gamma', 'time', 'time_step']
    for i in range(len(tmp_list)):
        tmp = True
        while tmp == True:
            try:
                tmp_list[i] = float(input(f'Enter {tmp_list[i]}: \n'))
                tmp = False
            except:
                print('Wrong input. ')
                continue
    return tmp_list


# Funkcja zapisująca dane w pliku podanym przez użytkownika
def save_data_to_file(t, y):
    name_of_file = input("Enter name of file: \n")
    data = {"t": t, "y": y}
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(name_of_file, index=False, sep='\t')


if __name__ == '__main__':
    list = taking_data()
    t, y = fading_sinusoid(list[0], list[1], list[2], list[3], list[4], int(list[5]))   #wywołanie funkcji z elementów z listy
    confirm = str(input('Do you want save data to file? [t/n]\n'))
    if confirm == 't' or 'T':
        save_data_to_file(t, y)

