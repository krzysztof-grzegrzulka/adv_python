class Student:
    def __init__(self, first_name, last_name, birth_date, city, street,
                 zip_code, phone):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone


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


class Order(Student, Employee):
    def __init__(self, employee, student, books, order_date):
        self.employee = employee  # pochodzi z Employee
        self.student = student  # pochodzi ze Student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return (f'Zamówenie złożone dla {self.student} przez {self.employee}' +
                f' na książki: {self._books}, dnia {self._order_date}')


class Book(Library):
    def __init__(self, library, publication_date, author_name, author_surname,
                 number_of_pages):
        self.library = library  # pochodzi z Library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self):
        return(f'Książka z {self.library} napisana przez {self._author_name}' +
               f' {self._author_surname}. Wydano ją {self._publication_date}' +
               f'. Ma {self._number_of_pages} stron.')


library1 = Library('Katowice', 'Książkowa 10', '40-555', '07:00-19:00',
                   '111-222-333')
library2 = Library('Mikołów', 'Piękna 2d', '40-234', '08:00-19:00',
                   '333-222-111')

# book1
# book2
# book3
# book4
# book5

employee1 = Employee('Jan', 'Kowalski', '01-02-2005', '03-10-1975', 'Katowice',
                     'Jasna 33/2', '40-678', '222-222-333')
employee2 = Employee('Janina', 'Nowak', '20-12-2010', '12-07-1990',
                     'Sosnowiec', 'Ciemna 12', '41-688', '100-200-444')
employee3 = Employee('Marian', 'Milusi', '24-05-1990', '10-10-1950',
                     'Dąbrowa Górnicza', 'Aleja Zwycięstwa 50a/4d', '39-666',
                     '554-332-335')

student1 = Student('Stefan', 'Wysoki', '12-12-1998', 'Katowice',
                   'Główna 10/55', '40-654', '778-556-326')
student2 = Student('Arleta', 'Kominiarz', '04-06-1999', 'Oświęcim', 'Zimna 33',
                   '42-601', '345-235-678')
student3 = Student('Sławomira', 'Pochopna', '20-08-1999', 'Milówka',
                   'Głośna 345', '30-776', '220-732-356')

# order1
# order2
# order3
