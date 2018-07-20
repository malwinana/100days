# Zadanie 0 - Name Generator - czyli generator imion.
# Najpierw należy zaimportować moduł random.
# Najprostszy sposób wykonania tego zadania, to zbudowanie listy imion i drugiej listy nazwisk . A następnie losowe wybranie imienia oraz nazwiska.
# Wersja ciut trudniejsza - można zbudować listy imion i nazwisk damskich i męskich, a następnie poprosić użytkownika o zdecydowanie czy ma to być imię i nazwisko damskie czy męskie. Do tego stosujemy instrukcje warunkowe if / elif.

import random

male_names = ['Adam', 'Mark', 'Ben', 'John', 'Mike', 'Randy', 'Chris']
female_names = ['Anna', 'Rita', 'Joana', 'Monica', 'Judy', 'Cristina', 'Veronica']
surnames = ['Johnson', 'Adams', 'Smith', 'Brodson', 'Williams', 'Taylor', 'Davies']

gender = input('Please select gender (M/F): ')

if gender == 'M':
    chosen_name = random.choice(male_names)
    chosen_surname = random.choice(surnames)

    print ("Generated name is: " + chosen_name + " "+ chosen_surname)

else:
    chosen_name = random.choice(female_names)
    chosen_surname = random.choice(surnames)

    print("Generated name is: " + chosen_name + " " + chosen_surname)