class Tarskereso:
    def __init__(self, sor) -> None:
        adatok = sor.strip().split(';')
        self.vezeteknev = adatok[0]
        self.keresztnev = adatok[1]
        self.kor = adatok[2]
        self.tavolsag_toled = int(adatok[3])
        self.nem = bool(adatok[4])      #0: nő   1: férfi
        self.keresett_nem = bool(adatok[5])
        self.keresett_kor_also_hatar = int(adatok[6])
        self.keresett_kor_felso_hatar = int(adatok[7])
        self.felhasznalonev = adatok[8]
        self.jelszo = adatok[9]