from classes.Dom import Dom


class Mieszkanie(Dom):
    def __init__(self, id_domu: str, adres: str, metraz: float,
                 cena_za_m: float, nr_mieszkania: str):
        super().__init__(id_domu, adres, metraz, cena_za_m)
        self._nr_mieszkania = nr_mieszkania

    @property
    def nr_mieszkania(self):
        return self._nr_mieszkania

    def __str__(self):
        return (
                f"Mieszkanie {self.id_domu} znajduje się w {self.adres}, nr" +
                f" mieszkania: {self.nr_mieszkania}. Ma {self.metraz} m2 " +
                f"i cenę za m2 {self.cena_za_m} zł")
