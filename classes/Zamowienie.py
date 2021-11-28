class Zamowienie:
    def __init__(self, id_zam: str, id_kl: str, adres_kl: str, miasto_kl: str,
                 liczba_szt: int, cena: float):
        self._id_zam = id_zam
        self._id_kl = id_kl
        self._adres_kl = adres_kl
        self._miasto_kl = miasto_kl
        self._liczba_szt = liczba_szt
        self._cena = cena

    @property
    def id_zam(self):
        return self._id_zam

    @property
    def id_kl(self):
        return self._id_kl

    @property
    def adres_kl(self):
        return self._adres_kl

    @property
    def miasto_kl(self):
        return self._miasto_kl

    @property
    def liczba_szt(self):
        return self._liczba_szt

    @property
    def cena(self):
        return self._cena

    @id_zam.setter
    def id_zam(self, id_zam):
        self._id_zam = id_zam

    @id_kl.setter
    def id_kl(self, id_kl):
        self._id_kl = id_kl

    @adres_kl.setter
    def adres_kl(self, adres_kl):
        self._adres_kl = adres_kl

    @miasto_kl.setter
    def miasto_kl(self, miasto_kl):
        self._miasto_kl = miasto_kl

    @liczba_szt.setter
    def liczba_szt(self, liczba_szt):
        self._liczba_szt = liczba_szt

    @cena.setter
    def cena(self, cena):
        self._cena = cena

    def wartosc_zamowienia(self):
        return round(self.liczba_szt * self.cena, 2)

    def adres_wysylki(self):
        return f'{self.adres_kl} {self.miasto_kl}'

    def __str__(self):
        return (f'Zamówienie o ID: {self.id_zam} złożone przez {self.id_kl} ' +
                f'na {self.liczba_szt} produktu po cenie {self.cena}/szt')
