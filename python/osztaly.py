class Tarskereso:
    def __init__(self, sor) -> None:
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.kor = adatok[1]
        self.tavolsag_toled = int(adatok[2])
        self.eletkor = adatok[3]
        self.nem = adatok[4]
        self.keresett_nem = adatok[5]
        self.keresett_kor = adatok[5]
