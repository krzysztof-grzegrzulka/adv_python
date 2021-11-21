class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f'Biblioteka w mieście {self.city}, kod: {self.zip_code}, ' +
                f'o adresie {self.street}. Godziny otwarcie: {self.open_hours}. ' +
                f'Telefon: {self.phone}')


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee  # pochodzi z Employee
        self.student = student  # pochodzi ze Student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return (f'Zamówenie złożone dla {self.student} przez {self.employee} ' +
                f'na książki: {self.books}, dnia {self.order_date}')


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'Pracownik {self.first_name} {self.last_name} urodzony ' +
                f'{self.birth_date} został zatrudniony {self.hire_date}. ' +
                f'Mieszka pod adresem {self.street} w {self.city}, ' +
                f'{self.zip_code}. Posiada telefon o numerze {self.phone}')


class Book:
    def __init__(self, library, publication_date, author_name, author_surname,
                 number_of_pages):
        self.library = library  # pochodzi z Library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return(f'Książka z {self.library} napisana przez {self.author_name} ' +
               f'{self.author_surname}. Wydano ją {self.publication_date}. ' +
               f'Ma {self.number_of_pages} stron.')
