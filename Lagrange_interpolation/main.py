import numpy as np
import matplotlib.pyplot as plt


# wielomian
def horner(x):
    # tu przekazujemy współczynniki wielomianu, od wsp. stojącego przy najwyższej potędze
    wsp = [1, 2, -5, -6]
    st = 3
    wynik = wsp[0]
    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]

    return wynik


def tryg(x):
    x = np.sin(2 * x)
    return x


def wykladnicza(x):
    return 2 ** x - 10



def zlozenie(x):
    return 3*(x**4) + np.tan(2*x)


# Ile węzłów potrzeba do interpolacji wielomianu N-tego stopnia?
# Dla danych n + 1 punktów pomiarowych, parami różnych od siebie, istnieje jedyny wielomian interpolujący stopnia co najwyżej n, zbudowany na tych punktach

# obliczenie wartosci argumentu funkcji
def calculateNode(x):
    for i in range(len(x)):
        x[i] = np.cos(np.pi * (2 * i + 1) / (2 * len(x) + 1))
    return x


# zmiana zmiennych przy zastosowaniu wartosci przedzialu [a,b]
def rescaling(x, a, b):
    return 1 / 2 * ((b - a) * x + (a + b))


def interpolacja(x, y, szukany_x):
    a = []
    fi = 1
    # pętla do wyliczania FI
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j: continue
            fi *= x[i] - x[j]
        a.append(y[i] / fi)
        fi = 1

    wynik = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j: continue
            fi *= szukany_x - x[j]

        wynik += a[i] * fi
        fi = 1

    return wynik


def rysuj_wykresy(funkcja, l_wezlow, lewy_kraniec, prawy_kraniec):
    x1 = calculateNode(list(range(1, l_wezlow + 1, 1)))
    y1 = list(range(l_wezlow))
    for i in range(l_wezlow):
        x1[i] = rescaling(x1[i], lewy_kraniec, prawy_kraniec)
        # print(f'X = {x1[i]}')
        y1[i] = funkcja(x1[i])
        # print(f'Y = {y1[i]}')

    x = np.linspace(lewy_kraniec, prawy_kraniec)
    y = funkcja(x)
    y2 = interpolacja(x1, y1, x)
    for i in range(len(x1)):
        plt.scatter(x1[i], y1[i], c="blue", s=50)
    if funkcja == tryg: plt.title("Funkcja sin(2x)")
    if funkcja == horner: plt.title("Funkcja x^3 + 2x^2 -5x -6")
    if funkcja == wykladnicza: plt.title("Funkcja 2^(x - 10)")
    if funkcja == zlozenie: plt.title("Funkcja log2x * sin(-2x) - 4")
    if funkcja == abs: plt.title("Funkcja |x|")
    # axes = plt.gca()
    # axes.set_ylim([-100, 100])
    plt.axvline(0)
    plt.axhline(0)
    plt.xlabel('X', fontsize=12, color='#323232')
    plt.ylabel('Y', fontsize=12, color='#323232')
    plt.plot(x, y, 'r', linewidth=5, label=f'Funkcja podstawowa')
    plt.plot(x, y2, 'g', linewidth=3, label=f'Funkcja interpolacyjna')

    plt.legend()

    plt.show()
