from osztalyok import *
# from login import *
from random import randint
import os

emberek: list[Tarskereso] = []


def main():
    beolvasas()
    '''valasztas = ''
    while valasztas != 'B' and valasztas != 'R':
        valasztas = input('Bejelentkezés(B) / Regisztráció(R): ')
    if valasztas == 'B':
        login()
    else:
        regisztracio()'''
    vezeteknev = input()
    keresztnev = input()
    kilep = False
    bejelentkezve_index = 0
    for i in range(0, len(emberek)):
        if emberek[i].keresztnev == keresztnev and emberek[i].vezeteknev == vezeteknev:
            bejelentkezve_index = i
            break
    opcio = ''
    while opcio != '0':
        os.system('cls')
        print('Opciók: ')
        print('\t1.: Emberek böngészése')
        print('\t2.: Szűrők változtatása')
        print('\t3.: Matchek megnézése')
        print('\t0.: Kilépés')
        opcio = input('Választásom: ')
        while opcio != '1' and opcio != '2' and opcio != '3' and opcio != '0':
            opcio = input('Választásom: ')
        match opcio:
            case '1':
                emberek_ajanlasa(emberek[bejelentkezve_index], bejelentkezve_index)
            case '2':
                szures(bejelentkezve_index)
            case '3':
                matcheim(bejelentkezve_index)
            case '0':
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



def emberek_ajanlasa(bejelentkezve: Tarskereso, bejelentkezve_index: int):
    f = open('matching.csv', 'r', encoding='utf-8')
    jobbra_huzottak: Match = []
    for sor in f:
        jobbra_huzottak.append(Match(sor))
    f.close()
    kilep = False
    index = 0
    van_ember = False
    while not kilep:
        kovetkezo = emberek[index]
        while not lehet(kovetkezo, bejelentkezve) and index < len(emberek)-1:
            index += 1
            kovetkezo = emberek[index]
        if index == len(emberek)-1 and not van_ember:
            print('Sajnos nincs számodra megfelelő felhasználó :( (próbáld meg változtatni a szűrőket)')
            input('<ENTER>')
            kilep = True
        elif index == len(emberek)-1 and valasztas != '':
            index = 0
        else:
            van_ember = True
            index += 1
            os.system('cls')
            print(f'{kovetkezo.vezeteknev} {kovetkezo.keresztnev}')
            print(f'Kor: {kovetkezo.kor}')
            print(f'Távolság tőled: {kovetkezo.tavolsag_toled} km')
            print(f'Gyerekek száma: {kovetkezo.gyerekek}')
            valasztas = input('\nBalra húz(B/b) / Jobbra húz(J/j) / Kilép(K/k): ').lower()
            while valasztas != 'b' and valasztas != 'j' and valasztas != 'k':
                valasztas = input('\nBalra húz(B) / Jobbra húz(J) / Kilép(K): ').lower()
            if valasztas == 'k':
                kilep = True
            elif valasztas == 'j':
                jobbra_huzottak[bejelentkezve_index].jobbra_huzottak.append(index)
            else:
                jobbra_huzottak[bejelentkezve_index].jobbra_huzottak.remove(index)
    





def szures(index: int):
    valasztas = ''
    while valasztas != '0':
        os.system('cls')
        print('Válassza ki, mit szeretne MÓDOSítani:')
        print(f'\t1.: Keresett kor alsó határ (jelenlegi: {emberek[index].keresett_kor_also_hatar} év)')
        print(f'\t2.: Keresett kor felső határ (jelenlegi: {emberek[index].keresett_kor_felso_hatar})')
        print(f'\t3.: Minimális gyerekszám (jelenlegi: {emberek[index].keresett_gyerek_also_hatar})')
        print(f'\t4.: Maximális gyerekszám (jelenlegi: {emberek[index].keresett_gyerek_felso_hatar})')
        print('\t0.: Kilépés')
        valasztas = input('Választásom: ')
        while valasztas != '1' and valasztas != '2' and valasztas != '3' and valasztas != '4' and valasztas != '0':
            valasztas = input('Választásom: ')
        match valasztas:
            case '1':
                uj = input('A keresett kor új alsó határa: ')
                while not uj.isdigit():
                    uj = input('A keresett kor új alsó határa: ')
                emberek[index].keresett_kor_also_hatar = int(uj)

            case '2':
                uj = input('A keresett kor új felső határa: ')
                while not uj.isdigit():
                    uj = input('A keresett kor új felső határa: ')
                emberek[index].keresett_kor_felso_hatar = int(uj)
            case '3':
                uj = input('Új minimális gyerekszám: ')
                while not uj.isdigit():
                    uj = input('Új minimális gyerekszám: ')
                emberek[index].keresett_gyerek_also_hatar = int(uj)
            case '4':
                uj = input('Új maximális gyerekszám: ')
                while not uj.isdigit():
                    uj = input('Új maximális gyerekszám: ')
                emberek[index].keresett_gyerek_felso_hatar = int(uj)
    kiiras()

    
def matcheim(bejelentkezve_index: int):
    f = open('python/matching.csv', 'r', encoding = 'utf-8')
    for sor in f:
        pass
    f.close()
            
        

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
        if int(korok[i]) > 25:
            gyerekek = randint(1, 4)
        else:
            gyerekek = 0
        keresett_also = randint(0, 4)
        keresett_felso = randint(keresett_also, 4)

        f.write(f'{vezeteknevek[i]};{keresztnevek[i]};{korok[i]};{tavolsagok[i]};{nemek[i]};{keresett_nemek[i]};{max(18, int(korok[i])-7)};{min(70, int(korok[i])+7)};{gyerekek};{keresett_felso};{keresett_also}\n')

def kiiras():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'w', encoding='utf-8')

    for e in emberek:
        f.write(f'{e.vezeteknev};{e.keresztnev};{e.kor};{e.tavolsag_toled};{int(e.nem)};{int(e.keresett_nem)};{e.keresett_kor_also_hatar};{e.keresett_kor_felso_hatar};{e.gyerekek};{e.keresett_gyerek_felso_hatar};{e.keresett_gyerek_also_hatar}\n')

    f.close()
    
def login_feltoltes():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    f2 = open('python/login.csv', 'w', encoding='utf-8')
    for sor in f:
        f2.write(f'{Tarskereso(sor).keresztnev};{Tarskereso(sor).keresztnev.lower()}123\n')


def matching_feltoltes():
    f = open('python/matching.csv', 'w', encoding='utf-8')
    for e in emberek:
        f.write(f'{e.vezeteknev};{e.keresztnev};\n')
    f.close()

main()