import numpy as np

# wielomian
def horner(x):
    # tu przekazujemy współczynniki wielomianu, od wsp. stojącego przy najwyższej potędze
    wsp = [1, 2, -5, -6]
    st = 3
    wynik = wsp[0]
    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]

    return np.exp(-x) * wynik


def horner2(x):
    # tu przekazujemy współczynniki wielomianu, od wsp. stojącego przy najwyższej potędze
    wsp = [1, 2, -5, -6]
    st = 3
    wynik = wsp[0]
    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]

    return wynik


def tryg(x):
    x = np.exp(-x) * np.sin(2 * x)
    return x


def tryg2(x):
    return np.sin(2 * x)


def wykladnicza(x):
    return np.exp(-x) * (2 ** x - 10)


def wykladnicza2(x):
    return 2 ** x - 10


def zlozenie(x):
    return np.exp(-x) * abs(x ** 5 + np.arctan(x) - 3)


def zlozenie2(x):
    return abs(x ** 5 + np.arctan(x) - 3)


def simpson(funkcja, a, b, m, epsilon):
    res1 = 0  # przechowuje wynik z poprzedniej iteracji
    res2 = 0  # przechowuje wynik z obecnej iteracji
    warunek = True
    licznik = 0
    while warunek:
        res1 = res2
        h = (b - a) / m
        suma1 = 0  # suma początków przedziału
        suma2 = 0  # suma środków przedziału

        # pętla odpowiedzialna za zliczanie poszczególnych sum
        for i in range(1, m):
            x = a + i * h
            suma1 += funkcja(x)  # początek i-tego przedziału
            suma2 += funkcja(x - (h / 2))  # środek i-1 przedziału

        suma2 += funkcja(b - (h / 2))
        # wybor przedzial zostal wybrany dla dowolnego przedzialu lub (0,nieskonczonosc)
        res2 = ((b - a) / (6 * m)) * (funkcja(a) + funkcja(b) + 2 * suma1 + 4 * suma2)
        # ponizej bedzie nieskonczonosc

        warunek = abs(res1 - res2) > epsilon
        m += 1
        licznik += 1
    return res2


def displaysimpson(funkcja, a, b, m, epsilon):
    if funkcja == tryg: f = "trygonometrycznej: sin(2x)"
    if funkcja == horner: f = "wielomianowej: x^3 + 2x^2 -5x -6"
    if funkcja == wykladnicza: f = "wykładniczej: 2^(x - 10)"
    if funkcja == zlozenie: f = "złożonej: |x^5 +arctan(x) -3|"
    print(f'Wynik całkowania funkcji {f} metodą Newtona-Cotesa na przedziale: [{a},{b}] = {simpson(funkcja, a, b, m, epsilon)}')


def simpson_0_to_inf(funkcja):
    wynik1 = 0
    wynik = 0
    a = 0
    w1 = True
    licznik = 0
    while w1:
        wynik = wynik1
        wynik1 += simpson(funkcja, a, a + 1, 1, 0.001)
        a += 1
        w1 = abs(wynik - wynik1) > 0.001
        licznik += 1
    if funkcja == tryg: f = "trygonometrycznej: sin(2x)"
    if funkcja == horner: f = "wielomianowej: x^3 + 2x^2 -5x -6"
    if funkcja == wykladnicza: f = "wykładniczej: 2^(x - 10)"
    if funkcja == zlozenie: f = "złożonej: |x^5 +arctan(x) -3|"
    print(f'Wynik całkowania funkcji {f} metodą Newtona-Cotesa na przedziale: [0,inf] = {wynik}')
    return wynik, licznik


wezly = np.array([
    [0.585786, 3.414214, 0, 0, 0],
    [0.415775, 2.29428, 6.289945, 0, 0],
    [0.322548, 1.745761, 4.53662, 9.395071, 0],
    [0.26356, 1.413403, 3.596426, 7.08581, 12.640801]
], dtype=np.float)

waga = np.array([[0.853553, 0.146447, 0, 0, 0],
                 [0.711093, 0.278518, 0.010389, 0, 0],
                 [0.603154, 0.357419, 0.038888, 0.000539, 0],
                 [0.521756, 0.398667, 0.075942, 0.003612, 0.000032]
                 ], dtype=np.float)


def gauss_laguerre(funkcja, waga, wezel, m, epsilon):
    res1 = 0  # przechowuje wynik z poprzedniej iteracji
    res2 = 0  # przechowuje wynik z obecnej iteracji
    warunek = True
    while warunek:
        if m > 4: break
        res1 = res2
        res2 = 0

        # pętla odpowiedzialna za zliczanie poszczególnych sum
        for i in range(m + 1):
            res2 += waga[m - 1][i] * funkcja(wezel[m - 1][i])
        # ponizej bedzie nieskonczonosc
        warunek = abs(res1 - res2) > epsilon
        m += 1
    if funkcja == tryg2: f = "trygonometrycznej: sin(2x)"
    if funkcja == horner2: f = "wielomianowej: x^3 + 2x^2 -5x -6"
    if funkcja == wykladnicza2: f = "wykładniczej: 2^(x - 10)"
    if funkcja == zlozenie2: f = "złożonej: |x^5 +arctan(x) -3|"
    print(f'Wynik całkowania funkcji {f} metodą Gaussa-Laguerrea na przedziale: [0,inf] = {res2}')
    return res2


# print(simpson(tryg,1,3,2,0.001))
# print("Wielomian:")
# displaysimpson(horner, 2, 15, 1, 0.001)
# simpson_0_to_inf(horner)[0]
# gauss_laguerre(horner2, waga, wezly, 1, 0.001)
#
# print("Trygonometryczna:")
# print("Simpson:        ", simpson_0_to_inf(tryg)[0])
# print("Gauss laguerre: ", gauss_laguerre(tryg2, waga, wezly, 1, 0.001))
#
# print("Wykładnicza:")
# print("Simpson:        ", simpson_0_to_inf(wykladnicza)[0])
# print("Gauss laguerre: ", gauss_laguerre(wykladnicza2, waga, wezly, 1, 0.001))
#
# print("Złożenie:")
# print("Simpson:        ", simpson_0_to_inf(zlozenie)[0])
# print("Gauss laguerre: ", gauss_laguerre(zlozenie2, waga, wezly, 1, 0.001))
