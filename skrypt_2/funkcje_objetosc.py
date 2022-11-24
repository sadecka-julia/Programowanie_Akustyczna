import math
import sys


def objetosc_kuli():
    r = float(input("Podaj promien kuli: "))
    return (4/3)*math.pi*(r**3)


def pole_kuli():
    r = float(input("Podaj promien kuli: "))
    return 4*math.pi*(r**2)


def masa_kuli():
    g = float(input("Podaj gestosc kuli: "))
    return g*objetosc_kuli()


def objetosc_czworoscian():
    a = float(input("Podaj długosc boku czworoscianu: "))
    return ((a**3)*(2**0.5))/12


def pole_czworoscianu():
    a = float(input("Podaj długosc boku czworoscianu: "))
    return (a**2)*(3**0.5)


def masa_czworoscianu():
    g = float(input("Podaj gestosc czworoscianu: "))
    return g*objetosc_czworoscian()


def objetosc_ostroslupa():
    a = float(input("Podaj dlugosc krawedzi podstawy: "))
    h = float(input("Podaj wysokosc"))
    return (1/3)*a*a*h


def pole_ostroslupa():
    a = float(input("Podaj dlugosc krawedzi podstawy: "))
    pp = a*a
    pb = a*(3**0.5)/2
    return pp+pb


def masa_ostroslupa():
    g = float(input("Podaj gestosc ostroslupa: "))
    return g*objetosc_ostroslupa()


def objetosc_stozka():
    r = float(input("Podaj promien podstawy: "))
    h = float(input("Podaj wysokosc staozka: "))
    return (math.pi*(r**2)*h)/3


def pole_stozka():
    r = float(input("Podaj promien podstawy: "))
    l = float(input("Podaj dlugosc tworzacej: "))
    return math.pi*r*(r+l)


def masa_stozka():
    g = float(input("Podaj gestosc stozka: "))
    return g*objetosc_stozka()


def objetosc_walca():
    r = float(input("Podaj promień walca: "))
    h = float(input("Podaj wysokosc walca: "))
    return math.pi*r*r*h


def pole_walca():
    r = float(input("Podaj promień walca: "))
    h = float(input("Podaj wysokosc walca: "))
    return 2*math.pi*r*(r+h)


def masa_walca():
    g = float(input("Podaj gestosc walca: "))
    return g+objetosc_walca()


def objetosc_elipsoidy():
    a = float(input("Podaj dluzsza półoś elipsoidy: "))
    b = float(input("Podaj krotsza półoś elipsoidy: "))
    return (4/3)*math.pi*a*b*b


def pole_elipsoidy():
    a = float(input("Podaj dluzsza półoś elipsoidy: "))
    b = float(input("Podaj krotsza półoś elipsoidy: "))
    e = (1-((b*b)/(a*a)))**0.5
    temp = b+((a/sys.float_info.epsilon)*(math.asin(e)))
    return 2*math.pi*b*temp


def masa_elipsoidy():
    g = float(input("Podaj gestosc elipsoidy: "))
    return g*objetosc_elipsoidy()


def wypisanie():
    print(60*'*', '\n', 'Wszystkie dlugosci podawaj w metrach, gestosc w [kg/m^3]\n', 60*'*', '\n')

    try:
        bryla = input('Wybierz bryle: kula [k], czworoscian prosty [c], stozek [s], walec [w], elipsoida [e]')
        czynnosc = input('Co chcesz wyliczyc: objetosc [o], mase [m], pole powierzchni [p]')

        if bryla == 'k' and czynnosc == 'o':
            print(f'Twoj wynik to: {objetosc_kuli()} m^3.')
        elif bryla == 'k' and czynnosc == 'm':
            print(f'Twoj wynik to: {masa_kuli()} kg.')
        elif bryla == 'k' and czynnosc == 'p':
            print(f'Twoj wynik to: {pole_kuli()} m^2.')

        elif bryla == 'c' and czynnosc == 'o':
            print(f'Twoj wynik to: {objetosc_czworoscian()} m^3.')
        elif bryla == 'c' and czynnosc == 'm':
            print(f'Twoj wynik to: {masa_czworoscianu()} kg.')
        elif bryla == 'c' and czynnosc == 'p':
            print(f'Twoj wynik to: {pole_czworoscianu()} m^2.')

        elif bryla == 'o' and czynnosc == 'o':
            print(f'Twoj wynik to: {objetosc_ostroslupa()} m^3.')
        elif bryla == 'o' and czynnosc == 'm':
            print(f'Twoj wynik to: {masa_ostroslupa()} kg.')
        elif bryla == 'o' and czynnosc == 'p':
            print(f'Twoj wynik to: {pole_ostroslupa()} m^2.')

        elif bryla == 's' and czynnosc == 'o':
            print(f'Twoj wynik to: {objetosc_stozka()} m^3.')
        elif bryla == 's' and czynnosc == 'm':
            print(f'Twoj wynik to: {masa_stozka()} kg.')
        elif bryla == 's' and czynnosc == 'p':
            print(f'Twoj wynik to: {pole_stozka()} m^2.')

        elif bryla == 'w' and czynnosc == 'o':
            print(f'Twoj wynik to: {objetosc_walca()} m^3.')
        elif bryla == 'w' and czynnosc == 'm':
            print(f'Twoj wynik to: {masa_walca()} kg.')
        elif bryla == 'w' and czynnosc == 'p':
            print(f'Twoj wynik to: {pole_walca()} m^2.')

        elif bryla == 'e' and czynnosc == 'o':
            print(f'Twoj wynik to: {objetosc_elipsoidy()} m^3.')
        elif bryla == 'e' and czynnosc == 'm':
            print(f'Twoj wynik to: {masa_elipsoidy()} kg.')
        elif bryla == 'e' and czynnosc == 'p':
            print(f'Twoj wynik to: {pole_elipsoidy()} m^2.')

        else:
            print('Podana wartosc nie istnieje:')

    except ValueError:
        print("Podana wartosc nie jest liczba")


if __name__ == '__main__':
    while True:
        wypisanie()
        x = input('Chcesz kontynuowac? Tak [t]/Nie [n]')
        if x == 'n' or x == 'N':
            exit()
