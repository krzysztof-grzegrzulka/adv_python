class KlientDetaliczny():
    def __init__(self, id_kl_det: str, imie: str, nazwisko: str,
                 adres_kl_det: str, nr_tel_kl_det: str):
        self._id_kl_det = id_kl_det
        self._imie = imie
        self._nazwisko = nazwisko
        self._adres_kl_det = adres_kl_det
        self._nr_tel_kl_det = nr_tel_kl_det

    @property
    def id_kl_det(self) -> str:
        return self._id_kl_det

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def adres_kl_det(self) -> str:
        return self._adres_kl_det

    @property
    def nr_tel_kl_det(self) -> str:
        return self._nr_tel_kl_det

    def __str__(self) -> str:
        return (f'Klient detaliczny o ID {self.id_kl_det} nazywa się ' +
                f'{self.imie} {self.nazwisko}. Mieszka na ' +
                f'{self.adres_kl_det}. Nr telefonu {self.nr_tel_kl_det}')
