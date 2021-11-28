class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return (f'Biblioteka w mieście {self._city}, kod: {self._zip_code}, ' +
                f'o adresie {self._street}. Godziny otwarcie: ' +
                f'{self._open_hours}. Telefon: {self._phone}')
