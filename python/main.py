from osztalyok import *
# from login import *
from random import randint
import os

emberek: list[Tarskereso] = []
matching: list[Match] = []


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
            
        
            




def beolvasas():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    for sor in f:
        emberek.append(Tarskereso(sor))
    f.close()
    f = open('python/matching.csv', 'r', encoding='utf-8')
    for sor in f:
        matching.append(Match(sor))
    f.close()



def lehet(szemely: Tarskereso, jelenlegi: Tarskereso):
    if szemely == jelenlegi or jelenlegi.keresett_nem != szemely.nem or jelenlegi.keresett_kor_also_hatar > szemely.kor or jelenlegi.keresett_kor_felso_hatar < szemely.kor:
        return False
    return True



def emberek_ajanlasa(bejelentkezve: Tarskereso, bejelentkezve_index: int):
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
            print(f'Foglalkozás: {kovetkezo.szakma}')
            valasztas = input('\nBalra húz(B/b) / Jobbra húz(J/j) / Kilép(K/k): ').lower()
            while valasztas != 'b' and valasztas != 'j' and valasztas != 'k':
                valasztas = input('\nBalra húz(B) / Jobbra húz(J) / Kilép(K): ').lower()
            if valasztas == 'k':
                kilep = True
            elif valasztas == 'j':
                if str(index) not in matching[bejelentkezve_index].jobbra_huzottak:
                    matching[bejelentkezve_index].jobbra_huzottak.append(str(index))
            else:
                if str(index) in matching[bejelentkezve_index].jobbra_huzottak:
                    matching[bejelentkezve_index].jobbra_huzottak.remove(str(index))
    
    matching_frissites(bejelentkezve)





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



def matching_frissites(bejelentkezve: Tarskereso):
    f = open('python/matching.csv', 'w', encoding='utf-8')
    for m in matching:
        jobbra = ''
        for j in m.jobbra_huzottak:
            if j != '':
                jobbra += str(j) + ','
        if len(jobbra) > 0:
            f.write(f'{m.vezeteknev};{m.keresztnev};{jobbra[0:-1]}\n')
        else:
            f.write(f'{m.vezeteknev};{m.keresztnev};\n')
    f.close()
    emberek.clear()
    matching.clear()
    beolvasas()




def matcheim(bejelentkezve_index: int):             # TODO
    print('Emberek, akikkel match-eltél: ')
    van = False
    for i in matching[bejelentkezve_index].jobbra_huzottak:
        if i != '':
            if str(bejelentkezve_index+1) in matching[int(i)-1].jobbra_huzottak:
                print(f'\t{matching[int(i)-1].vezeteknev} {matching[int(i)-1].keresztnev} - {emberek[int(i)-1].teloszam}')
                van = True
    if not van:
        print('senki:(')
    input('<ENTER>')

            
        

def randomolas():
    szakmak = ['könyvelő', 'pultos', 'séf', 'programozó', 'cégvezető', 'parlamenti képviselő', 'ügyvéd', 'pedagógus', 'újságíró', 'bolti eladó', 'buszvezető', 'autóvezetés-oktató', 'lakberendező', 'műsorvezető', 'építészmérnök', 'szállodai recepciós', 'nincs', 'árufeltöltő', 'közmunkás', 'vállalkozó']
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'w', encoding='utf-8')
    for e in emberek:
        telefonszam = ''
        print(e.keresett_kor_felso_hatar)
        for i in range(9):
            telefonszam += str(randint(0,9))
        f.write(f'{e.vezeteknev};{e.keresztnev};{e.kor};{e.tavolsag_toled};{e.nem};{e.keresett_nem};{e.keresett_kor_also_hatar};{e.keresett_kor_felso_hatar};{e.gyerekek};{e.keresett_gyerek_felso_hatar};{e.keresett_gyerek_also_hatar};{szakmak[randint(0,19)]};06{telefonszam}\n')
    f.close()

def kiiras():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'w', encoding='utf-8')

    for e in emberek:
        f.write(f'{e.vezeteknev};{e.keresztnev};{e.kor};{e.tavolsag_toled};{int(e.nem)};{int(e.keresett_nem)};{e.keresett_kor_also_hatar};{e.keresett_kor_felso_hatar};{e.gyerekek};{e.keresett_gyerek_felso_hatar};{e.keresett_gyerek_also_hatar};{e.szakma};{e.teloszam}\n')

    f.close()
    
def login_feltoltes():
    f = open('python/szingli_anyukak_es_apukak_es_gyerekek.csv', 'r', encoding='utf-8')
    f2 = open('python/login.csv', 'w', encoding='utf-8')
    for sor in f:
        f2.write(f'{Tarskereso(sor).keresztnev};{Tarskereso(sor).keresztnev.lower()}123\n')


def matching_feltoltes():
    f = open('python/matching.csv', 'w', encoding='utf-8')
    for e in emberek:
        f.write(f'{e.vezeteknev};{e.keresztnev};{e.teloszam};\n')
    f.close()

main()