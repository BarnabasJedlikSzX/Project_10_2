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
    bejelentkezve: Tarskereso = None
    for e in emberek:
        if e.felhasznalonev == login.felhasznalonev:
            bejelentkezve = e
            break 
    index = 0
    volt = False
    valasztas = ''
    while not kilep:
        kovetkezo = emberek[index]
        while not lehet(kovetkezo, bejelentkezve) and index < len(emberek)-1:
            index += 1
            kovetkezo = emberek[index]
        if index == len(emberek)-1 and valasztas == '':
            print('Sajnos nincs számodra megfelelő felhasználó :(')
            kilep = True
        elif index == len(emberek)-1 and valasztas != '':
            index = 0
        else:
            volt = True
            index += 1
            os.system('cls')
            print(f'{kovetkezo.vezeteknev} {kovetkezo.keresztnev}')
            print(f'Kor: {kovetkezo.kor}')
            print(f'Távolság tőled: {kovetkezo.tavolsag_toled} km')
            valasztas = input('\nBalra húz(B) / Jobbra húz(J) / Kilép(K): ')
            while valasztas != 'B' and valasztas != 'J' and valasztas != 'K':
                valasztas = input('\nBalra húz(B) / Jobbra húz(J) / Kilép(K): ')
            if valasztas == 'K':
                kilep = True
            elif valasztas == 'B':
                pass
            else:
                pass
            
        
            

    


def beolvasas():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    for sor in f:
        emberek.append(Tarskereso(sor))
    f.close()

def lehet(szemely: Tarskereso, jelenlegi: Tarskereso):
    if szemely == jelenlegi or jelenlegi.keresett_nem != szemely.nem or jelenlegi.keresett_kor_also_hatar > szemely.kor or jelenlegi.keresett_kor_felso_hatar < szemely.kor:
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