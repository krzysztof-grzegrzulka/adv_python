from classes.Book import Book
# import classes.Book as Book
from classes.Employee import Employee
# import classes.Employee as Employee
from classes.Flat import Flat
# import classes.Flat as Flat
from classes.House import House
# import classes.House as House
from classes.Library import Library
# import classes.Library as Library
from classes.Order import Order
# import classes.Order as Order
from classes.Property import Property
import classes.Property as Property
from classes.Student import Student

# import classes.Student as Student


# Zadanie 1
student1 = Student("Jan", 65)
student2 = Student("Janina", 40)

print(student1.is_passed)
print(student2.is_passed)

# Zadanie 2
library1 = Library('Katowice', 'Książkowa 10', '40-555', '07:00-19:00',
                   '111-222-333')
library2 = Library('Mikołów', 'Piękna 2d', '40-234', '08:00-19:00',
                   '333-222-111')

book1 = Book('Katowice', 'Książkowa 10', '40-555', '07:00-19:00',
             '111-222-333', '12-12-2000', 'Adam', 'Mickiewicz', '450')
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

student1 = Student('Stefan Wysoki', '55')
student2 = Student('Arleta Kominiarz', '76')
student3 = Student('Sławomira Pochopna', '24')

# order1
# order2
# order3


# Zadanie 3
house = House('osiedle mieszkaniowe', 2, '250000', 'Czerwona 3', '1000')
flat = Flat('apartamentowiec', 3, '500000', 'Niebieska 3a/12', '10')

print(house)
print(flat)
