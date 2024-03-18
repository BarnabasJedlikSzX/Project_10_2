from Tarskererso import Tarskereso
import os
from random import randint

userAdatok = []

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
    jelszo = input('\tJelszó: ')
    jelszo2 = input('\tJelszó mégegyszer: ')
    while jelszo != jelszo2:
        print('\tA két jelszó nem egyezik.')
        jelszo = input('\tJelszó: ')
        jelszo2 = input('\tJelszó mégegyszer: ')
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
    # lakhely = input('\tLakhely (Város): ')
    tavolsagToled = randint(1, 100)
    '''
    userAdatok += vezeteknev
    userAdatok += keresztnev
    userAdatok += str(kor)
    userAdatok += str(tavolsagToled)
    userAdatok += nem
    userAdatok += keresettNem
    userAdatok += tavolsagToled
    '''
    userAdatok.append(vezeteknev)
    userAdatok.append(keresztnev)
    userAdatok.append(str(kor))
    userAdatok.append(str(tavolsagToled))
    userAdatok.append(nem)
    userAdatok.append(keresettNem)
    userAdatok.append(keresettKorAlso)
    userAdatok.append(keresettKorFelso)
    userAdatok.append(felhasznalonev)
    userAdatok.append(jelszo)
    # userAdatok += lakhely
    f = open('szingli_anyukak_es_apukak_es_gyerekek.csv','w', encoding = 'utf-8')
    for sor in userAdatok:
        f.write(f'{userAdatok[0]};{userAdatok[1]};{userAdatok[2]};{userAdatok[3]};{userAdatok[4]};{userAdatok[5]};{userAdatok[6]};{userAdatok[7]};{userAdatok[8]};{userAdatok[9]}\n')
    f.close()
    userAdatok.clear()
    input('<ENTER>')
    



regisztracio()
