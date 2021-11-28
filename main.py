from classes.Produkt import Produkt
from classes.Magazyn import Magazyn
from classes.KlientDetaliczny import KlientDetaliczny
from classes.Zamowienie import Zamowienie
from classes.KlientBiznesowy import KlientBiznesowy

zamowienie1 = Zamowienie('as-2333', 'jkow321', 'Dluga 15a', 'Mikolow', 12, 100)

print(zamowienie1.adres_wysylki())
print(zamowienie1.wartosc_zamowienia())
