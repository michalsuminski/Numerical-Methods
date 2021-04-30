from tkinter import filedialog
from logic import *
from tkinter import *

root = Tk()
root.title("Metoda iteracyjna Jacobiego")

# POLA TEKSTOWE
e_input = Text(root, font=("Helvetica", 20), width=30, height=10)
e_output = Text(root, font=("Helvetica", 20), width=30, height=10)
e_input.grid(row=0, rowspan=2, column=0, columnspan=2, padx=10, pady=10)
e_output.grid(row=0, rowspan=2, column=5, columnspan=2, padx=10, pady=10)

# Przycisk czytający wspolczynniki z pliku
button_read_from_file_input = Button(root, text="Odczytaj z pliku", width=20, height=2, bd=5,
                                     command=lambda: e_input.insert(INSERT, read_from_file(
                                         filedialog.askopenfilename(initialdir="./", title="Select file"))))
button_read_from_file_input.grid(row=2, column=0)

# Przycisk potwierdzający zmiane
button_change_matrix = Button(root, text="Zmień", width=20, height=2, bd=5,
                                     command=lambda: string_to_matrix(e_input.get("1.0", END)))
button_change_matrix.grid(row=2, column=1)

# Etykieta do pobrania liczby wiersz
Label(root, text="Podaj liczbę iteracji: ", font=("Helvetica", 15)).grid(row=0, column=2, pady=5)

# Okno do wpisania liczby iteracji
textbox_iterations = Entry(root, font=("Helvetica", 10), width=10)
textbox_iterations.grid(row=0, column=3, pady=8, ipady=3)

# Przycisk potwierdzający iteracje
button_confirm_iterations = Button(root, text="Rozwiąż", width=10, bd=5,
                                   command=lambda: e_output.insert(INSERT, method(coefficients, results, int(textbox_iterations.get()), None)))
button_confirm_iterations.grid(row=0, column=4, padx=10)

# Etykieta do pobrania dokładności (epsilona)
Label(root, text="Podaj epsilon: ", font=("Helvetica", 15)).grid(row=1, column=2, pady=5)

# Okno do wpisania epsilona
textbox_epsilon = Entry(root, font=("Helvetica", 10), width=10)
textbox_epsilon.grid(row=1, column=3, pady=8, ipady=3)

# Przycisk potwierdzający epsilon
button_confirm_epsilon = Button(root, text="Rozwiąż", width=10, bd=5,
                                command=lambda: e_output.insert(INSERT, method(coefficients, results, None, float(textbox_epsilon.get()))))
button_confirm_epsilon.grid(row=1, column=4, padx=10)

title = Label(root, text="Michał Sumiński 230013, Jan Płoszaj 229985", font=("Helvetica", 15))
title.grid(row=3, column=2, columnspan=3)

root.mainloop()
