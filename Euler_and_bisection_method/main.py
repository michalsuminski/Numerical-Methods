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
    np.seterr(divide='ignore')
    return np.log2(x) * np.sin(-2 * x) - 4


def bisekcja(lewy, prawy, epsilon, l_iteracji, funkcja):
    # warunek sprawdzający czy funkcja przyjmuje różne znaki na końcach przedziału
    if funkcja(lewy) * funkcja(prawy) >= 0:
        print("Podano niewłaściwy przedział!")
        return -1
    # jesli kryterium stopu jest epsilon to:
    if epsilon != None:
        wynik = (lewy + prawy) / 2
        if funkcja(wynik) == 0:
            return wynik
        else:
            warunek = True
            while warunek:
                if funkcja(lewy) * funkcja(wynik) < 0:
                    prawy = wynik
                if funkcja(prawy) * funkcja(wynik) < 0:
                    lewy = wynik
                res = (lewy + prawy) / 2
                warunek = abs(res - wynik) > epsilon
                wynik = res
            return res

    else:
        wynik = (lewy + prawy) / 2
        if funkcja(wynik) == 0:
            return wynik
        else:
            for i in range(l_iteracji):
                if funkcja(lewy) * funkcja(wynik) < 0:
                    prawy = wynik
                if funkcja(prawy) * funkcja(wynik) < 0:
                    lewy = wynik
                res = (lewy + prawy) / 2
                wynik = res
            return res


# METODA SIECZNYCH

# WAŻNY KOMENTARZ: Dodatkowo w przedziale [a,b] pierwsza pochodna f '(x) jest różna od zera. Nie istnieje zatem
# minimum lub maksimum lokalne. Ten warunek gwarantuje nam, iż sieczna nie będzie równoległa do osi OX,
# co uniemożliwiłoby wyznaczenie jej punktu przecięcia z tą osią --> CZYLI MUSIMY PODAĆ TAKI PRZEDZIAŁ, ABY FUNKCJA
# NIE MIAŁA NA TYM PRZEDZIALE EKSTREMUM LOKALNEGO
def sieczna(lewy, prawy, epsilon, l_iteracji, funkcja):
    if funkcja(lewy) * funkcja(prawy) >= 0:
        print("Podano niewłaściwy przedział!")
        return -1
    fjeden = funkcja(lewy)
    fdwa = funkcja(prawy)
    if epsilon != None:
        while True:
            wynik = lewy - (fjeden * (lewy - prawy) / (fjeden - fdwa))
            fzero = funkcja(wynik)
            prawy = lewy
            fdwa = fjeden
            lewy = wynik
            fjeden = fzero
            res = lewy - (fjeden * (lewy - prawy) / (fjeden - fdwa))
            if abs(res - wynik) < epsilon:
                return res
    else:
        # uważać na odpowiednia liczbę iteracji, ponieważ występuje dzielenie przez przy bardzo małych wartościach
        for i in range(l_iteracji):
            wynik = lewy - (fjeden * (lewy - prawy) / (fjeden - fdwa))
            fzero = funkcja(wynik)
            prawy = lewy
            fdwa = fjeden
            lewy = wynik
            fjeden = fzero
        return wynik


while True:
    print("Wybierz funkcję: \n"
          "1.wielomian\n"
          "2.trygonometryczna\n"
          "3.wykładnicza\n"
          "4.złożenie")

    num = int(input("Podaj numer 1-4: "))

    # podanie przedziału

    left = float(input("Podaj lewy kraniec: "))
    right = float(input("Podaj prawy kraniec: "))

    # podanie kryterium zakończenia

    print("Podaj kryterium zakończenia algorytmu: \n"
          "1. Warunek nałożony na dokładność (epsilon) \n"
          "2. Liczba iteracji")

    endcrit = int(input("Podaj numer 1-2: "))
    if endcrit == 1:
        iteracje = None
        epsilon = float(input("Podaj epsilon: "))

    else:
        epsilon = None
        iteracje = int(input("Podaj liczbę iteracji: "))

    if num == 1:
        print("Wyniki dla funkcji wielomianowej: f(x) = x^3 + 2x^2 -5x -6:")
        w_bisekcja = bisekcja(left, right, epsilon, iteracje, horner)
        w_siecznych = sieczna(left, right, epsilon, iteracje, horner)
        print("Metodą bisekcji: " + str(w_bisekcja) + " (czerwona kropka)")
        print("Metodą siecznych: " + str(w_siecznych) + " (zielona kropka)" + "\n")

        x = np.linspace(left, right)
        y = horner(x)
        plt.scatter(w_bisekcja, horner(w_bisekcja), c="red", s=50)
        plt.scatter(w_siecznych, horner(w_siecznych), c="green", s=50)
        plt.title("Funkcja wielomianowa")
        plt.axvline(0)
        plt.axhline(0)
        plt.xlabel('X', fontsize=12, color='#323232')
        plt.ylabel('Y', fontsize=12, color='#323232')
        plt.plot(x, y, 'r')

        plt.show()

    if num == 2:
        print("Wyniki dla funkcji trygonometrycznej: f(x) = sin2x:")
        w_bisekcja = bisekcja(left, right, epsilon, iteracje, tryg)
        w_siecznych = sieczna(left, right, epsilon, iteracje, tryg)
        print("Metodą bisekcji: " + str(w_bisekcja) + " (czerwona kropka)")
        print("Metodą siecznych: " + str(w_siecznych) + " (zielona kropka)" + "\n")

        x = np.linspace(left, right)
        y = tryg(x)
        plt.scatter(w_bisekcja, tryg(w_bisekcja), c="red", s=50)
        plt.scatter(w_siecznych, tryg(w_siecznych), c="green", s=50)
        plt.title("Funkcja trygonometryczna")
        plt.axvline(0)
        plt.axhline(0)
        plt.xlabel('X', fontsize=12, color='#323232')
        plt.ylabel('Y', fontsize=12, color='#323232')
        plt.plot(x, y, 'r')

        plt.show()

    if num == 3:
        print("Wyniki dla funkcji wykładniczej: f(x) = 2^(x-1) -4:")
        w_bisekcja = bisekcja(left, right, epsilon, iteracje, wykladnicza)
        w_siecznych = sieczna(left, right, epsilon, iteracje, wykladnicza)
        print("Metodą bisekcji: " + str(w_bisekcja) + " (czerwona kropka)")
        print("Metodą siecznych: " + str(w_siecznych) + " (zielona kropka)" + "\n")

        x = np.linspace(left, right)
        y = wykladnicza(x)
        plt.scatter(w_bisekcja, wykladnicza(w_bisekcja), c="red", s=50)
        plt.scatter(w_siecznych, wykladnicza(w_siecznych), c="green", s=50)
        plt.title("Funkcja wykładnicza")
        plt.axvline(0)
        plt.axhline(0)
        plt.xlabel('X', fontsize=12, color='#323232')
        plt.ylabel('Y', fontsize=12, color='#323232')
        plt.plot(x, y, 'r')

        plt.show()

    if num == 4:
        print("Wyniki dla funkcji złożonej: f(x) = log2(x) * sin(-2x) -4:")
        w_bisekcja = bisekcja(left, right, epsilon, iteracje, zlozenie)
        w_siecznych = sieczna(left, right, epsilon, iteracje, zlozenie)
        print("Metodą bisekcji: " + str(w_bisekcja) + " (czerwona kropka)")
        print("Metodą siecznych: " + str(w_siecznych) + " (zielona kropka)")

        x = np.linspace(left, right)
        y = zlozenie(x)
        plt.scatter(w_bisekcja, zlozenie(w_bisekcja), c="red", s=50)
        plt.scatter(w_siecznych, zlozenie(w_siecznych), c="green", s=50)
        plt.title("Funkcja złożona")
        plt.axvline(0)
        plt.axhline(0)
        plt.xlabel('X', fontsize=12, color='#323232')
        plt.ylabel('Y', fontsize=12, color='#323232')
        plt.plot(x, y, 'r')

        plt.show()
