class ZwiazekWedkarski:

    def __init__(self, miejscowosc):
        self.miejscowosc = miejscowosc
        self.wodyZwiazku = []

    def podniesJakoscWody(self, woda, ilosc):
        if(ilosc > 0):
            if(woda in self.wodyZwiazku):
                woda.increaseQuality(ilosc)

    def getWodyZwiazku(self):
        return self.wodyZwiazku

    def nadajZwzwolenie(self, wedkarz, liczba):
        wedkarz.setZezwolenie(liczba)

    def dodajWode(self, woda):
        self.wodyZwiazku.append(woda)