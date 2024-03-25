class Tarskereso:
    def __init__(self, sor) -> None:
        adatok = sor.strip().split(';')
        self.vezeteknev = adatok[0]
        self.keresztnev = adatok[1]
        self.kor = int(adatok[2])
        self.tavolsag_toled = int(adatok[3])
        self.nem = bool(adatok[4]=='1')      #0: nő   1: férfi
        self.keresett_nem = bool(adatok[5]=='1')
        self.keresett_kor_also_hatar = int(adatok[6])
        self.keresett_kor_felso_hatar = int(adatok[7])
        self.gyerekek = int(adatok[8])
        self.keresett_gyerek_felso_hatar = int(adatok[9])
        self.keresett_gyerek_also_hatar = int(adatok[10])