from osztaly import Tarskereso
from loginAdatok import Data
import os
from random import randint
import pwinput

userAdatok = []
login: Data = None

def main():
    v = input()
    match v:
        case '1':
            login()
        case '2':
            regisztracio()

def login():
    os.system('cls')
    global login
    # print('\nFelhasználónév')
    # print('-----------------')
    nev = input('Felhasználónév: ')
    # print('-----------------')
    # print('\nJelszó')
    # print('-----------------')
    jelszo = pwinput.pwinput(prompt='Jelszó: ', mask='*')
    # print('-----------------')
    f = open('jelszavak.csv', 'r', encoding = 'utf-8')
    van = False
    for sor in f:
        loginAdatok = Data(sor)
        if loginAdatok.felhasznalonev == nev and loginAdatok.jelszo == jelszo:
            print('Sikeres belépés')
            input('<ENTER>')
            van = True
            break
        if loginAdatok.felhasznalonev == nev and loginAdatok.jelszo != jelszo:
            os.system('cls')
            print('Hibás jelszó')
            input('<ENTER>')
            login()
    if not van:
        os.system('cls')
        print('Nincs ilyen felhasználó')
        input('<ENTER>')
        login()
    


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
    rejtettJelszo = hash(jelszo)
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
    userAdatok.append(vezeteknev)
    userAdatok.append(keresztnev)
    userAdatok.append(str(kor))
    userAdatok.append(str(tavolsagToled))
    userAdatok.append(nem)
    userAdatok.append(keresettNem)
    userAdatok.append(keresettKorAlso)
    userAdatok.append(keresettKorFelso)
    # userAdatok.append(felhasznalonev)
    # userAdatok.append(jelszo)
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv','w', encoding = 'utf-8')
    f.write(f'{userAdatok[0]};{userAdatok[1]};{userAdatok[2]};{userAdatok[3]};{userAdatok[4]};{userAdatok[5]};{userAdatok[6]};{userAdatok[7]}\n')
    f.close()
    userAdatok.clear()
    f = open('login.csv', 'w', encoding = 'utf-8')
    f.write(f'{felhasznalonev};{rejtettJelszo}\n')
    f.close()
    input('<ENTER>')
    

'''
def login_feltoltes():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    f2 = open('python/login.csv', 'w', encoding='utf-8')
    hashelt = None
    for sor in f:
        hashelt = hash(f'{Tarskereso(sor).keresztnev.lower()}123')
        f2.write(f'{Tarskereso(sor).keresztnev};{hashelt}\n')
'''

main()
