import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# #Odczyt danych z pliku .csv za pomoca biblioteki pandas
# df = pd.read_csv (r'dane_pomiarowe.csv', sep="\t")
# #Rzutowanie danych z kolumny z czasem i kolumny z przyśpieszeniem na wektory
# np.array
# t =np.array(df['t'])
# a =np.array(df['a'])

# # wykres a(t)
# xpoints = np.array(t)
# ypoints = np.array(a)
#
# plt.scatter(xpoints, ypoints, color = '#88c999')
# plt.show()

# # zapisanie danych do pliku
# t = np.linspace(-10, 10, 100) #generuje wektor 100 liczb rzeczywistych od -10 do 10
# y = t*t
# data = {"t": t, "y": y} #tworzy słownik klucz-wartość przechowujący dane
# dataframe = pd.DataFrame(data) #tworzy pandas dataframe
# dataframe.to_csv("Nowy_plik_z_danymi.csv", index = False, sep='\t')

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#Generowanie punktów funkcji kwadratowej
a = 2
b = -7
amp = 10 #amplitida szumu
x = np.linspace(-10,10,100) #dziedzina funkcji
y= a*x**2+b + amp*(np.random.rand(len(x))-0.5) #zbiór wartości x=y**2 plus szum
# Fitowanie funkcji
def func(x, a, b):
 return a*x**2+b #funkcja fitująca parabolę
p0=[1, 1] #wektor inicjalizujący
fit_params, covariance_matrix = curve_fit(func, x, y, p0=p0) #fitowanie
# Parametry fitowania
print("parametry fitowania: \na=", fit_params[0], "\nb=", fit_params[1])
# Wyświetlanie wykresów
plt.scatter(x,y) #Wygenerowane punkty
plt.plot(x, func(x, *fit_params), 'r') #Wykres funkcji dopasowania
plt.show()


