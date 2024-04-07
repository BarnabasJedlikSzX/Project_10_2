class Tarskereso:
    def __init__(self, sor) -> None:
        adatok = sor.strip().split(';')
        self.vezeteknev = adatok[0]
        self.keresztnev = adatok[1]
        self.kor = int(adatok[2])
        self.tavolsag_toled = int(adatok[3])
        self.nem = adatok[4]     #0: nő   1: férfi
        self.keresett_nem = adatok[5]
        self.keresett_kor_also_hatar = int(adatok[6])
        self.keresett_kor_felso_hatar = int(adatok[7])
        self.gyerekek = int(adatok[8])
        self.keresett_gyerek_felso_hatar = int(adatok[9])
        self.keresett_gyerek_also_hatar = int(adatok[10])
        self.szakma = adatok[11]
        self.teloszam = adatok[12]

class Match:
    def __init__(self,sor:str):
        adatok = sor.strip().split(';')
        self.vezeteknev = adatok[0]
        self.keresztnev = adatok[1]
        self.jobbra_huzottak = adatok[2].strip().split(',')
        