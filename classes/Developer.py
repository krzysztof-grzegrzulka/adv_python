class Developer:
    def __init__(self, nazwa_dev: str, rok_zalozenia: str, miasto_dev: str,
                 liczba_pracownikow: int):
        self._nazwa_dev = nazwa_dev
        self._rok_zalozenia = rok_zalozenia
        self._miasto_dev = miasto_dev
        self.liczba_pracownikow = liczba_pracownikow

    @property
    def nazwa_dev(self):
        return self._nazwa_dev

    @property
    def rok_zalozenia(self):
        return self._rok_zalozenia

    @property
    def miasto_dev(self):
        return self._miasto_dev

    def __str__(self):
        return (
                f"{self.nazwa_dev} jest deweloperem z {self.miasto_dev}. " +
                f"Firma została założona w {self.rok_zalozenia} i zatrudnia" +
                f" {self.liczba_pracownikow} pracowników")
