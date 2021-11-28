# import classes.Library as Library
from classes.Library import Library


class Book(Library):
    def __init__(self, city, street, zip_code, open_hours, phone,
                 publication_date, author_name, author_surname,
                 number_of_pages):
        super().__init__(city, street, zip_code, open_hours, phone)
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self):
        return (f'Książka z biblioteki w {self.city} na ulicy {self.street}' +
                f' napisana przez {self._author_name} ' +
                f'{self._author_surname}. Wydano ją {self._publication_date}' +
                f'. Ma {self._number_of_pages} stron.')
