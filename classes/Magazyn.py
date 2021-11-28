class Magazyn:
    def __init__(self, id_mag: str, nazwa_mag: str, miasto_mag: str,
                 adres_mag: str, nr_tel_mag: str):
        self._id_mag = id_mag
        self._nazwa_mag = nazwa_mag
        self._miasto_mag = miasto_mag
        self._adres_mag = adres_mag
        self._nr_tel_mag = nr_tel_mag

    @property
    def id_mag(self) -> str:
        return self._id_mag

    @property
    def nazwa_mag(self) -> str:
        return self._nazwa_mag

    @property
    def miasto_mag(self) -> str:
        return self._miasto_mag

    @property
    def adres_mag(self) -> str:
        return self._adres_mag

    @property
    def nr_tel_mag(self) -> str:
        return self._nr_tel_mag

    def __str__(self) -> str:
        return (f'Magazyn {self.nazwa_mag} o ID {self.id_mag}, znajduje się ' +
                f'w {self.adres_mag}, {self.miasto_mag}. Nr telefonu: ' +
                f'{self.nr_tel_mag}')
