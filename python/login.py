from osztalyok import *
from loginAdatok import Data
import os
from random import randint
import pwinput
import hashlib

userAdatok = []
login: Data = None
emberek: list[Tarskereso] = []
infok: list[Data] = []
matchek: list[Match] = []

def login():
    os.system('cls')
    global login
    nev = input('Felhasználónév: ')
    jelszo = pwinput.pwinput(prompt='Jelszó: ', mask='*')
    encoded = jelszo.encode('utf-8')
    hashelt = hashlib.sha256(encoded).hexdigest()
    f = open('python/login.csv', 'r', encoding = 'utf-8')
    van = False
    counter = 0
    for sor in f:
        loginAdatok = Data(sor)
        if loginAdatok.felhasznalonev == nev and loginAdatok.jelszo == hashelt:
            print('Sikeres belépés')
            input('<ENTER>')
            van = True
            break
        if loginAdatok.felhasznalonev == nev and loginAdatok.jelszo != hashelt:
            os.system('cls')
            print('Hibás jelszó')
            input('<ENTER>')
            login()
        counter += 1
    if not van:
        os.system('cls')
        print('Nincs ilyen felhasználó')
        input('<ENTER>')
        login()
    return counter
    
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
    encoded = jelszo.encode('utf-8')
    rejtettJelszo = hashlib.sha256(encoded).hexdigest()
    kor = int(input('\tKor: '))
    while kor < 18:
        print('\tA program használatához legalább 18 évesnek kell lennie.')
        kor = int(input('\tKor: '))
    nem = input('\tNem (ferfi v. no): ').lower()
    while nem != 'ferfi' and nem != 'no':
        print('\tKérjük a két opció közül adjon meg egyet és ne használjon ékezetes karaktereket')
        nem = input('\tNem (ferfi v. no): ')
    if nem == 'ferfi':
        nem = '1'
    else:
        nem = '0'
    gyerekSzam = szamBekeres('\tGyerekek száma: ')
    keresettGyerekMin = szamBekeres('\tKeresett gyerekek száma (min.): ')
    keresettGyerekMax = szamBekeres('\tKeresett gyerekek száma (max): ')
    keresettKorAlso = int(input('\tKeresett kor (alsó határ, min. 18): '))
    while keresettKorAlso < 18:
        print('\tA programban nincsenek 18 év alatti felhasználók')
        keresettKorAlso = int(input('\tKeresett kor (alsó határ, min. 18): '))
    keresettKorFelso = (input('\tKeresett kor (felső határ): '))
    keresettNem = input('\tKeresett nem: ')
    if keresettNem == 'ferfi':
        keresettNem = '1'
    else:
        keresettNem = '0'
    teloszam = szamBekeres('\tTelefonszám: ')
    szakma = input('\tSzakma: ')
    tavolsagToled = randint(1, 100)
    userAdatok.append(vezeteknev)
    userAdatok.append(keresztnev)
    userAdatok.append(str(kor))
    userAdatok.append(str(tavolsagToled))
    userAdatok.append(nem)
    userAdatok.append(keresettNem)
    userAdatok.append(keresettKorAlso)
    userAdatok.append(keresettKorFelso)
    userAdatok.append(gyerekSzam)
    userAdatok.append(keresettGyerekMax)
    userAdatok.append(keresettGyerekMin)
    userAdatok.append(szakma)
    userAdatok.append(teloszam)
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    for sor in f:
        emberek.append(Tarskereso(sor))
    f.close()
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv','w', encoding = 'utf-8')
    for e in emberek:
        f.write(f'{e.vezeteknev};{e.keresztnev};{e.kor};{e.tavolsag_toled};{int(e.nem)};{int(e.keresett_nem)};{e.keresett_kor_also_hatar};{e.keresett_kor_felso_hatar};{e.gyerekek};{e.keresett_gyerek_felso_hatar};{e.keresett_gyerek_also_hatar};{e.szakma};{e.teloszam}\n')
    f.write(f'{userAdatok[0]};{userAdatok[1]};{userAdatok[2]};{userAdatok[3]};{userAdatok[4]};{userAdatok[5]};{userAdatok[6]};{userAdatok[7]};{userAdatok[8]};{userAdatok[9]};{userAdatok[10]};{userAdatok[11]};{userAdatok[12]}\n')
    f.close()
    f = open('python/login.csv', 'r', encoding='utf-8')
    for sor in f:
        infok.append(Data(sor))
    f.close()
    f = open('python/login.csv', 'w', encoding = 'utf-8')
    for i in infok:
        f.write(f'{i.felhasznalonev};{i.jelszo}\n')
    f.write(f'{felhasznalonev};{rejtettJelszo}\n')
    f.close()

    f = open('python/matching.csv', 'r', encoding='utf-8')
    for sor in f:
        matchek.append(Match(sor))
    f.close()

    f = open('python/matching.csv', 'w', encoding='utf-8')
    for m in matchek:
        jobbra = ''
        for j in m.jobbra_huzottak:
            if j != '':
                jobbra += str(j) + ','
        if len(jobbra) > 0:
            f.write(f'{m.vezeteknev};{m.keresztnev};{jobbra[0:-1]}\n')
        else:
            f.write(f'{m.vezeteknev};{m.keresztnev};\n')
    f.write(f'{userAdatok[0]};{userAdatok[1]};\n')
    f.close()
    userAdatok.clear()
    input('<ENTER>')
    
def login_feltoltes():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    f2 = open('python/login.csv', 'w', encoding='utf-8')
    hashelt = None
    for sor in f:
        jelszo = f'{Tarskereso(sor).keresztnev.lower()}123'.encode('utf-8')
        hashelt = hashlib.sha256(jelszo).hexdigest()
        f2.write(f'{Tarskereso(sor).keresztnev};{hashelt}\n')

def szamBekeres(kerdes: str):
    szam = input(kerdes)
    try:
        szam = int(szam)
    except:
        szamBekeres()
    return szam

