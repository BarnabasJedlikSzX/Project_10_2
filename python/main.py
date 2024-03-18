from osztaly import Tarskereso
from login import *
from random import randint
import os

emberek: list[Tarskereso] = []

def main():
    beolvasas()
    valasztas = ''
    while valasztas != 'B' and valasztas != 'R':
        valasztas = input('Bejelentkezés(B) / Regisztráció(R): ')
    if valasztas == 'B':
        login()
    else:
        regisztracio()
    kilep = False
    index = 0
    bejelentkezve: Tarskereso = None
    for e in emberek:
        if e.felhasznalonev == login.nev:
            bejelentkezve = e
            break 
    while not kilep:
        kovetkezo = emberek[index]
        if lehet(kovetkezo, bejelentkezve):     # felajánlhatja az embert
            os.system('cls')
            print(f'{kovetkezo.vezeteknev} {kovetkezo.keresztnev}')
            print(f'Kor: {kovetkezo.kor}')
            print(f'Távolság tőled: {kovetkezo.tavolsag_toled} km')
            

    


def beolvasas():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    for sor in f:
        emberek.append(Tarskereso(sor))
    f.close()

def lehet(szemely: Tarskereso, jelenlegi: Tarskereso):
    if szemely == jelenlegi or jelenlegi.keresett_nem != szemely.nem or jelenlegi.keresett_kor_also_hatar < szemely.kor or jelenlegi.keresett_kor_felso_hatar > szemely.kor:
        return False
    return True

def randomolas():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    vezeteknevek: list[str] = []
    keresztnevek: list[str] = []
    korok: list[str] = []
    nemek: list[str] = []
    keresett_nemek: list[str] = []
    tavolsagok: list[str] = []
    for sor in f:
        adatok = sor.strip().split(';')
        vezeteknevek.append(adatok[0])
        keresztnevek.append(adatok[1])
        korok.append(adatok[2])
        tavolsagok.append(adatok[3])
        nemek.append(adatok[4])
        keresett_nemek.append(adatok[5])
    f.close()
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'w', encoding='utf-8')
    for i in range(0, 50):

        f.write(f'{vezeteknevek[i]};{keresztnevek[i]};{korok[i]};{tavolsagok[i]};{nemek[i]};{keresett_nemek[i]};{max(18, int(korok[i])-7)};{min(70, int(korok[i])+7)};{keresztnevek[i]};{keresztnevek[i].lower()}123\n')
    

main()