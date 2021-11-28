class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self):
        return (f'Pracownik {self._first_name} {self._last_name} urodzony ' +
                f'{self._birth_date} został zatrudniony {self._hire_date}. ' +
                f'Mieszka pod adresem {self._street} w {self._city}, ' +
                f'{self._zip_code}. Posiada telefon o numerze {self._phone}')
