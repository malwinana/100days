# Age in Seconds - oblicz swój wiek w sekundach.
# Tu przydatne będzie zaimportowanie date z modułu datetime.
# Pewnym utrudnieniem (chyba) jest poproszenie, aby użytkownik wpisał date swoich urodzin.


import datetime
user_date = ' '

while True:
    user_date = input("Please provide your birthdate in a format YYYY-MM-DD: ")
    try:
        birth_date = datetime.datetime.strptime(user_date, '%Y-%m-%d')
        difference = (datetime.datetime.now() - birth_date).total_seconds()
        print('You are {0} seconds old.'.format(difference))
        # print('You are ' + difference + ' seconds old!')
        if difference < 0:
            print('Are you from the future?')
        break

    except:
        print('Incorect data format!')

