from tkinter import filedialog
from main import *
from tkinter import *

FUNKCJA = 1 # domyślnie trygonometryczna

def ustaw_numer(x):
    global FUNKCJA
    if x == 1: FUNKCJA = 1
    if x == 2: FUNKCJA = 2
    if x == 3: FUNKCJA = 3
    if x == 4: FUNKCJA = 4
    if x == 5: FUNKCJA = 5

def wybor_funkcji_gauss(x):
    if x == 1: return tryg2
    if x == 2: return horner2
    if x == 3: return wykladnicza2
    if x == 4: return zlozenie2

def wybor_funkcji_simpson(x):
    if x == 1: return tryg
    if x == 2: return horner
    if x == 3: return wykladnicza
    if x == 4: return zlozenie

def operation():
    if len(e_prawy_kraniec.get()) == 0:
        simpson_0_to_inf(wybor_funkcji_simpson(FUNKCJA))
        gauss_laguerre(wybor_funkcji_gauss(FUNKCJA), waga, wezly, 1, float(e_epsilon.get()))
    else:
        displaysimpson(wybor_funkcji_simpson(FUNKCJA), float(e_lewy_kraniec. get()), float(e_prawy_kraniec.get()), 1, float(e_epsilon.get()))

root = Tk()
root.title("Metody całkowania numerycznego")
# root.configure(background="#f7cbc8")

label_funkcja = Label(root, anchor="w", text="Wybierz funkcję:", font=("Helvetica", 20), width=17)
label_funkcja.grid(row=0, column=0, ipady=10)


# Radialbuttony do wybrania odpowiedniej funkcji
var = IntVar()
button_tryg = Radiobutton(root, variable=var, value=1, text="sin(2x)", font=("Helvetica", 15),  width=20, bd=5, command=lambda: ustaw_numer(1))
button_tryg.grid(row=0, column=1)

button_wiel = Radiobutton(root, variable=var, value=2, text="x^3 + 2x^2 -5x -6", font=("Helvetica", 15), width=20, bd=5, command=lambda: ustaw_numer(2))
button_wiel.grid(row=0, column=2)

button_wyk = Radiobutton(root, variable=var, value=3, text="2^(x - 10)", font=("Helvetica", 15), width=20, bd=5, command=lambda: ustaw_numer(3))
button_wyk.grid(row=0, column=3)

button_zloz = Radiobutton(root, variable=var, value=4, text="|x^5 +arctan(x) -3|", font=("Helvetica", 15), width=20, bd=5, command=lambda: ustaw_numer(4))
button_zloz.grid(row=0, column=4)

label_lewy_kraniec = Label(root, anchor="w", text="Podaj lewy kraniec:", font=("Helvetica", 20), width=17)
label_lewy_kraniec.grid(row=1, column=0, ipady=10)

e_lewy_kraniec = Entry(root, font=("Helvetica", 18), width=10)
e_lewy_kraniec.grid(row=1, column=1, padx=10, pady=10)

label_prawy_kraniec = Label(root, anchor="w", text="Podaj prawy kraniec:", font=("Helvetica", 20), width=17)
label_prawy_kraniec.grid(row=2, column=0, ipady=10)

e_prawy_kraniec = Entry(root, font=("Helvetica", 18), width=10)
e_prawy_kraniec.grid(row=2, column=1, padx=10, pady=10)

label_epsilon = Label(root, anchor="w", text="Podaj epsilon:", font=("Helvetica", 20), width=17)
label_epsilon.grid(row=3, column=0, ipady=10)

e_epsilon = Entry(root, font=("Helvetica", 18), width=10)
e_epsilon.grid(row=3, column=1, padx=10, pady=10)

# Przycisk zatwierdzający wybrane ustawienia, oraz wywołujący funkcję z maina
button_zbadaj = Button(root, text="Zbadaj", font=("Helvetica", 15), bg="blue", fg="white",
                       command=lambda: operation())
button_zbadaj.grid(row=3, column=4, columnspan=2)

title = Label(root, text="Michał Sumiński 230013, Jan Płoszaj 229985", font=("Helvetica", 15))
title.grid(row=4, column=2, columnspan=2)

root.mainloop()