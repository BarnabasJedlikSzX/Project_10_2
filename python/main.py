from osztaly import Tarskereso
from login import login
import os

emberek: list[Tarskereso] = []

def main():
    beolvasas()
    nev = login()
    kilep = False
    index = 0
    bejelentkezve: Tarskereso = None
    for e in emberek:
        if e.felhasznalonev == nev:
            bejelentkezve = e
            break 
    while not kilep:
        kovetkezo = emberek[index]
        if lehet(kovetkezo, bejelentkezve):     # felajánlhatja az embert
            os.system('cls')
            print(f'{kovetkezo.vezeteknev} {kovetkezo.keresztnev}')
            print(f'Kor: {kovetkezo.kor}')
            

    


def beolvasas():
    f = open('szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    for sor in f:
        emberek.append(Tarskereso(sor))
    f.close()

def lehet(szemely: Tarskereso, jelenlegi):
    if szemely == jelenlegi or jelenlegi.keresett_nem != szemely.nem or jelenlegi.keresett_kor_also_hatar < szemely.kor or jelenlegi.keresett_kor_felso_hatar > szemely.kor:
        return False
    

main()