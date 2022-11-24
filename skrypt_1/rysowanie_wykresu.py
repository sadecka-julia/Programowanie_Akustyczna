import matplotlib.pyplot as plt
import numpy as np


def print_operation(a, b, c, d):
    arr = [a, b, c, d]
    arr_with_sign = []

    for i in range(len(arr)):
        if arr[i] > 0:
            arr_with_sign.append('+'+str(arr[i]))
        else:
            arr_with_sign.append(str(arr[i]))

    print(a, "*x^3", arr_with_sign[1], "*x^2", arr_with_sign[2], "*x", arr_with_sign[3], sep='')


def take_range():
    try:
        od = int(input("Podaj poczatek zakresu: "))
        do = int(input("Podaj koniec zakresu: "))
    except ValueError:
        print("Wprowadzona wartosc nie jest liczba")
        quit()

    if od >= do:
        print("Poczatek zakresu musi byc mniejszy niz koniec!")
        quit()

    return od, do


def print_figure(a, b, c, d, od, do):
    X = np.linspace(od, do, 100)
    Y = a*(X**3)+b*(X**2)+c*X+d
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(X, Y)
    plt.show()


if __name__ == '__main__':
    a = int(input("Podaj parametr przy x^3:\n"))
    b = int(input("Podaj parametr przy x^2:\n"))
    c = int(input("Podaj parametr przy x:\n"))
    d = int(input("Podaj parametr wyrazu wolnego:\n"))
    print_operation(a, b, c, d)
    od, do = take_range()
    print_figure(a, b, c, d, od, do)
