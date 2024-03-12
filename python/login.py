from osztaly import Tarskereso
import os
from random import randint

userAdatok: str = ''

def login():
    print('\nFelhasználónév')
    # print('-----------------')
    nev = input('')
    # print('-----------------')
    print('\nJelszó')
    # print('-----------------')
    jelszo = ('Jelszó: ')
    # print('-----------------')

def regisztracio():
    global userAdatok
    os.system('cls')
    print('Regisztráció')
    vezeteknev = input('\tVezetéknév: ')
    keresztnev = input('\tKeresztnév: ')
    felhasznalonev = input('\tFelhasználónév: ')
    kor = int(input('\tKor: '))
    while kor < 18:
        print('\tA program használatához legalább 18 évesnek kell lennie.')
        kor = int(input('\tKor: '))
    nem = input('\tNem (ferfi v. no): ').lower()
    while nem != 'ferfi' and nem != 'no':
        print('\tKérjük a két opció közül adjon meg egyet és ne használjon ékezetes karaktereket')
        nem = input('\tNem (ferfi v. no): ')
    keresettKorAlso = int(input('\tKeresett kor (alsó határ, min. 18): '))
    while keresettKorAlso < 18:
        print('\tA programban nincsenek 18 év alatti felhasználók')
        keresettKorAlso = int(input('\tKeresett kor (alsó határ, min. 18): '))
    keresettKorFelso = (input('\tKeresett kor (felső határ): '))
    keresettNem = input('\tKeresett nem: ')
    lakhely = input('\tLakhely (Város): ')
    tavolsagToled = randint(1, 100)
    userAdatok += vezeteknev
    userAdatok += keresztnev
    userAdatok += str(kor)
    userAdatok += str(tavolsagToled)
    userAdatok += nem
    userAdatok += keresettNem
    



regisztracio()
