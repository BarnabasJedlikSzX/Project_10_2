from osztaly import Tarskereso

userAdatok: list[Tarskereso] = []

def login():
    print('\nFelhasználónév')
    print('-----------------')
    nev = input('')
    print('-----------------')
    print('\nJelszó')
    print('-----------------')
    jelszo = input('')
    print('-----------------')

login()