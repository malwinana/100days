# Higher/Lower - gra, w której użytkownik zgaduje liczbę, a komputer mu podpowiada, czy liczba jest większa od podanej czy mniejsza. Określamy w jakim przedziale ma być
# ta liczba i ile rund ma toczyć się gra.
# lub:
# Heads/Tails - orzeł czy reszka - komputer oblicza prawdopodobieństwo wypadnięcia orła np. w 100 rzutach i sprawdza, czy jest to zgodne z naszym przewidywaniem
# (czy zgadliśmy ile razy wypadnie np.orzeł).

import random
rounds = int(input("How many rounds do you want? "))
random_number = random.randint(0,10)

for i in range(rounds):
    user_number = int(input('Please guesss the number from 0 to 10: '))
    print('Your choice is ', user_number)

    if user_number < random_number:
        print("Your number is smaller than the target value!")
        print(rounds -i -1, "chances left\n")

    elif user_number > random_number:
        print("Your value is greater than targer value!")
        print(rounds - i - 1, "chances left\n")

    elif user_number == random_number:
        print('You guess it!')
        break
    else:
        print('Please enter an integer, you lost your turn!')
        print(rounds - i - 1, "chances left\n")





