import matplotlib.pyplot as plt
import numpy as np

try:
    od = int(input("Podaj poczatek zakresu: "))
    do = int(input("Podaj koniec zakresu: "))
except ValueError:
    print("Wprowadzona wartosc nie jest liczba")
    quit()

if od >= do:
    print("Poczatek zakresu musi byc mniejszy niz koniec!")
    quit()

X = np.linspace(-10, 10, 100)
Y = np.sin(X)

plt.plot(X, Y)
plt.show()
