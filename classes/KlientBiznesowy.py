class KlientBiznesowy():
    def __init__(self, id_kl_fir: str, nazwa_fir: str, miasto_fir: str,
                 adres_fir: str, nr_tel_fir: str):
        self._id_kl_fir = id_kl_fir
        self._nazwa_fir = nazwa_fir
        self._miasto_fir = miasto_fir
        self._adres_fir = adres_fir
        self._nr_tel_fir = nr_tel_fir

    @property
    def id_kl_fir(self) -> str:
        return self._id_kl_fir

    @property
    def nazwa_fir(self) -> str:
        return self._nazwa_fir

    @property
    def miasto_fir(self) -> str:
        return self._miasto_fir

    @property
    def adres_fir(self) -> str:
        return self._adres_fir

    @property
    def nr_tel_fir(self) -> str:
        return self._nr_tel_fir

    def __str__(self) -> str:
        return (f'Klient biznesowy o ID {self.id_kl_fir} nazywa się ' +
                f'{self.nazwa_fir}. Jego siedziba znajduje się w ' +
                f'{self.miasto_fir} pod adresem {self.adres_fir}. Nr tel: ' +
                f'{self.nr_tel_fir}')
