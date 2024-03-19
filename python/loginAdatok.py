class Data:

    def __init__(self, sor: str):
        adatok = sor.strip().split(';')
        self.felhasznalonev = adatok[0]
        self.jelszo = adatok[1]