class Wedka:

    def __init__(self, rodzaj, jakosc):
        rodzaje = []
        rodzaje.append("splawik")
        rodzaje.append("grunt")
        rodzaje.append("spinning")
        self.jakosc = jakosc
        if(rodzaj in rodzaje):
            self.rodzaj = rodzaj
        else:
            print("Podano zły rodzaj wędki")

    def getJakosc(self):
        return self.jakosc

    def getRodzaj(self):
        return self.rodzaj