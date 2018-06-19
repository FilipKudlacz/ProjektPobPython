from random import randint

class Rzeka:

    def __init__(self, _nazwa, _jakoscWody, _liczbaRyb, _ryby):
        self.nazwa = _nazwa
        self.jakoscWody = _jakoscWody
        self.liczbaRyb = _liczbaRyb
        self.ryby = _ryby
        self.typ = 1

    def sprobujZlapac(self, wedka):
        if self.jakoscWody < 6 :
            wiecej = 6 - self.jakoscWody
            print("Łowisko zamknięte z powodu zbyt słabej jakości wody. Zwiększ jakoś wody przynajmniej o " + str(wiecej) + ".")
            return 0;
        elif self.liczbaRyb > 0 :
            for ryba in self.ryby:
                random = randint(1, 100)
                if ryba.szansaZlapania(wedka) >= random:
                    self.liczbaRyb = self.liczbaRyb -1
                    return ryba
        else:
            print("W rzece " + self.nazwa + " nie ma już ryb.")
        return 0

    def getName(self):
        return self.nazwa

    def getQuality(self):
        return self.jakoscWody

    def increaseQuality(self, liczba):
        self.jakoscWody = self.jakoscWody + liczba
        if self.jakoscWody > 10 :
            self.jakoscWody = 10

    def getFN(self):
        return self.liczbaRyb

    def jestMiejsce(self):
        return True

    def getType(self):
        return int(self.typ)

    def increaseFN(self, ile):
        self.liczbaRyb = self.liczbaRyb + ile
    def zajmijStanowisko(self):
        return 1