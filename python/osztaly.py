class Tarskereso:
    def __init__(self, sor) -> None:
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.kor = adatok[1]
        self.lakohely = adatok[2]
        self.eletkor = adatok[3]