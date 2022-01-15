class Zamowienie:
    def __init__(self, id_zam: str, id_domu: str, metraz: float,
                 cena_za_m: float):
        self._id_zam = id_zam
        self._id_domu = id_domu
        self._metraz = metraz
        self._cena_za_m = cena_za_m

    @property
    def id_zam(self):
        return self._id_zam

    @property
    def id_domu(self):
        return self._id_domu

    @property
    def metraz(self):
        return self._metraz

    @property
    def cena_za_m(self):
        return self._cena_za_m

    @id_zam.setter
    def id_zam(self, id_zam):
        self._id_zam = id_zam

    @id_domu.setter
    def id_domu(self, id_domu):
        self._id_domu = id_domu

    @metraz.setter
    def metraz(self, metraz):
        self._metraz = metraz

    @cena_za_m.setter
    def cena_za_m(self, cena_za_m):
        self._cena_za_m = cena_za_m

    def wartosc_zamowienia(self):
        return round(self.metraz * self.cena_za_m, 2)

    def lacznie_metrow(self):
        return self.metraz

    def __str__(self):
        return (
                f"Zamówienie o ID: {self.id_zam} składa się z domu " +
                f"{self.id_domu} o powierzchni {self.metraz} m2 i cenie " +
                f"za m2 {self.cena_za_m} zł. Łączna wartość zamówienia " +
                f"wynosi {self.wartosc_zamowienia()}. Łącznie metrów: " +
                f"{self.lacznie_metrow()}")
