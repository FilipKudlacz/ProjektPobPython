from Ryba import Ryba
from ZwiazekWedkarski import ZwiazekWedkarski
from Wedka import Wedka
from Wedkarz import Wedkarz
from Rzeka import Rzeka
from Jezioro import Jezioro
from StawPrywatny import StawPrywatny

szczupak = Ryba("szczupak")
sum = Ryba("sum")
okon = Ryba("okon")
drapiezne = []

drapiezne.append(szczupak)
drapiezne.append(sum)
drapiezne.append(okon)

wedka = Wedka("spinning", 1)

kiekrz = Jezioro("Kierskie", 8 , 120, 30, drapiezne)
warta = Rzeka("Warta", 3 , 300, drapiezne)
blazeja = StawPrywatny("Blazeja",9 ,40,20,drapiezne, "728465914")

Ja = Wedkarz(1, wedka, 1)

ZWPoznan = ZwiazekWedkarski("Poznan")
ZWPoznan.nadajZwzwolenie(Ja,3)
ZWPoznan.dodajWode(warta)
ZWPoznan.podniesJakoscWody(warta, 2)

Ja.idzNadWode(warta);
print("Jestem nad " + Ja.getGdzie().getName())
Ja.zlapRybe()

ZWPoznan.podniesJakoscWody(warta, 3)
ZWPoznan.getWodyZwiazku()[ZWPoznan.getWodyZwiazku().index(warta)].increaseFN(20)

Ja.zlapRybe()

Ja.idzNadWode(kiekrz)
print("Jestem nad " + Ja.getGdzie().getName())
Ja.zlapRybe()
