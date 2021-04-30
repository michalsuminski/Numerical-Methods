import numpy as np
# from view import *

# macierz, zawierająca współczynniki
coefficients = []

# macierz zawierająca wyniki
results = []


def read_from_file(filename):
    matrix = []
    with open(filename) as f:
        text = f.read()
        # po odczytaniu danych z pliku odpowiednio je formatujemy
        string_to_matrix(text)
    return text


# metoda zamieniająca string na macierz
def string_to_matrix(text):
    coefficients.clear()
    results.clear()
    # pomocnicza tablica do wierszy we współczynnikach
    row = []
    mapped = text.strip().split("\n")
    for line in mapped:
        splitted_line = line.strip().split(",")
        for i in range(len(splitted_line)):
            if i == len(splitted_line) - 1:
                results.append(float(splitted_line[i]))
            else:
                row.append(float(splitted_line[i]))
        coefficients.append(row)
        row = []
    # print(coefficients)
    # print(results)


# metoda sprawdzająca zbieżność macierzy, czyli czy jest macierzą przekatniowo dominujacą
def check_convergence(matrix):
    sumDiag = 0
    sumRows = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                sumDiag += abs(matrix[i][j])
            else:
                sumRows += abs(matrix[i][j])
        # kiedy macierz nie jest zbieżna zwraca fałsz
        if sumDiag <= sumRows:
            return 0
        sumDiag = 0
        sumRows = 0
    # kiedy jest zbieżna prawda
    return 1


def inverse_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = matrix[i][j] ** -1
    # print(matrix)
    return matrix


def opposite(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0: continue
            matrix[i][j] = -matrix[i][j]
    return matrix


# podzielenie wejsciowej macierzy na macierze L D U
def divide_matrix_on_LDU(matrix):
    L = np.copy(matrix)
    D = np.copy(matrix)
    U = np.copy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                # L jest macierzą w której znajdują się elementy których numer wiersza jest większy od numeru kolumny
                # D to macierz diagonalna z elementami tylko na głównej przekątnej
                D[i][j] = 0
                # U jest macierzą w której znajdują się elementy których numer wiersza jest większy od numeru kolumny
                U[i][j] = 0
            elif j > i:
                L[i][j] = 0
                D[i][j] = 0
            elif i == j:
                L[i][j] = 0
                U[i][j] = 0

    # Mnożenie macierzy odwrotnej do D i sumy L i U
    M = opposite(np.matmul(inverse_matrix(D), np.add(L, U)))

    # print(L)
    # print(D)
    # print(U)
    # print(np.add(L, U))
    # print(D)
    # print(inverse_matrix(D))
    # print(M)

    return M


M = divide_matrix_on_LDU([[1, 0.2, 0.3], [0.1, 1, -0.3], [-0.1, -0.2, 1]])


# matrixM --> przekształcona macierz współczynników
# result --> wyniki układu równań
# matrixA --> macierz współczynników
def method(matrixA, result, iter, epsilon):
    # jeśli warunek zbieżności nie spełniony to stosowny komunikat i przerwanie funkcji
    if not check_convergence(matrixA):
        return 'Macierz nie jest zbieżna, podaj inną macierz!'

    # macierz A dzielimy na sumę macierzy i tworzymy macierz M
    matrixM = divide_matrix_on_LDU(matrixA)

    # obliczenie potrzebnych ilorazow bedacych wartosciami w poszczegolnych rownianiach
    tab = []
    for i in range(len(result)):
        tab.append(result[i] / matrixA[i][i])
    pom = 0
    tab_x = [0 for i in range(len(matrixA))]
    tab_pom = [0 for i in range(len(matrixA))]
    if epsilon is None:
        for i in range(iter):
            for j in range(len(matrixM)):
                for k in range(len(matrixM)):
                    if j == k:
                        continue
                    pom += matrixM[j][k] * tab_x[k]
                pom += tab[j]
                tab_pom[j] = pom
                pom = 0
            tab_x = tab_pom
    else:
        condition = True
        while condition:
            flag = False
            for j in range(len(matrixM)):
                for k in range(len(matrixM)):
                    if j == k:
                        continue
                    pom += matrixM[j][k] * tab_x[k]
                pom += tab[j]
                tab_pom[j] = pom
                pom = 0

            for i in range(len(tab_x)):
                # jesli co najmniej jeden x nie spelnia warunku to idziemy dalej
                if abs(tab_x[i] - tab_pom[i]) > epsilon:
                    flag = True
            condition = flag
            tab_x = np.copy(tab_pom)
    # print(tab_x)
    formatted_result = ''
    for index, value in enumerate(tab_x):
        formatted_result += f"x{index+1}={value:>3}\n"
    return formatted_result

