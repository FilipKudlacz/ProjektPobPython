class Wedkarz:

    def __init__(self, id, wedka, zezwolenie):
        self.id = id
        self.wedka = wedka
        self.zezwolenie = zezwolenie

    def idzNadWode(self, woda):
        if woda.jestMiejsce()==True and int(str(woda.getType())) <= int(self.zezwolenie):
            self.stanowisko = woda.zajmijStanowisko()
            self.gdzie = woda
        else:
            woda.zajmijStanowisko()

    def zlapRybe(self):
        zlapana = self.gdzie.sprobujZlapac(self.wedka)
        if zlapana != 0 :
            print("Został złapany " + str(zlapana.getNazwa()) + ", ta ryba ma " + str(zlapana.getWielkosc()) + "kg. Gratulacje!")


    def setZezwolenie(self, liczba):
        self.zezwolenie = liczba


    def getGdzie(self):
        return self.gdzie