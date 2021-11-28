class Produkt:
    def __init__(self, nazwa_prod: str, kategoria: str, cena: float,
                 kolor: str, data_wprowadzenia: str):
        self._nazwa_prod = nazwa_prod
        self._kategoria = kategoria
        self._cena = cena
        self._kolor = kolor
        self._data_wprowadzenia = data_wprowadzenia

    @property
    def nazwa_prod(self) -> str:
        return self._nazwa_prod

    @property
    def kategoria(self) -> str:
        return self._kategoria

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def kolor(self) -> str:
        return self._kolor

    @property
    def data_wprowadzenia(self) -> str:
        return self._data_wprowadzenia

    def __str__(self) -> str:
        return (f'Produkt {self.nazwa_prod} kosztuje {self.cena}, jest ' +
                f'koloru {self.kolor}. Jest z kategorii {self.kategoria} . ' +
                f'Został wprowadzony do sprzedaży w {self.data_wprowadzenia}')
