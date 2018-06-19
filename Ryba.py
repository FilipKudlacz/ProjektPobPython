from random import randint

class Ryba:
    def __init__(self, nazwa):
        self.nazwa =  nazwa

        if nazwa == "szczupak":
            self.szansaDrap = 30
            self.szansaNDrap = 0
            self.wielkosc = randint(1, 8)
        elif nazwa == "okon":
            self.szansaDrap = 20
            self.szansaNDrap = 25
            self.wielkosc = randint(1,3)
        elif nazwa == "sum":
            self.szansaDrap = 10
            self.szansaNDrap = 30
            self.wielkosc = randint(1, 31)
        elif nazwa == "karp":
            self.szansaDrap = 0
            self.szansaNDrap = 40
            self.wielkosc = randint(1, 10)
        elif nazwa == "lin":
            self.szansaDrap = 40
            self.szansaNDrap = 0
            self.wielkosc = randint(1, 4)
        else:
            self.szansaDrap=0
            self.szansaNDrap=0
            self.wielkosc = 0

    def szansaZlapania(self, wedka):
        if wedka.getRodzaj() == "splawik" or wedka.getRodzaj() == "grunt" :
            return self.szansaNDrap * wedka.getJakosc()
        elif wedka.getRodzaj() == "spinning" :
            return self.szansaDrap * int(wedka.getJakosc())
        else:
            return 0

    def getWielkosc(self):
        return self.wielkosc

    def getNazwa(self):
        return self.nazwa
