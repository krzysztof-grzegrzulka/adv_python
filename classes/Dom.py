class Dom:
    def __init__(self, id_domu: str, adres: str, metraz: float,
                 cena_za_m: float):
        self._id_domu = id_domu
        self._adres = adres
        self._metraz = metraz
        self._cena_za_m = cena_za_m

    @property
    def id_domu(self):
        return self._id_domu

    @property
    def adres(self):
        return self._adres

    @property
    def metraz(self):
        return self._metraz

    @property
    def cena_za_m(self):
        return self._cena_za_m

    def __str__(self):
        return (
                f"Dom {self.id_domu} znajduje się w {self.adres}. Ma " +
                f"{self.metraz} m2 i cene za m2 {self.cena_za_m} zł")
