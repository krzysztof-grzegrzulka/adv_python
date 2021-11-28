import classes.Book as Book
import classes.Employee as Employee
import classes.Flat as Flat
import classes.House as House
import classes.Library as Library
import classes.Order as Order
import classes.Property as Property
import classes.Student as Student

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

student1 = Student('Stefan Wysoki', '12-12-1998', 'Katowice',
                   'Główna 10/55', '40-654', '778-556-326')
student2 = Student('Arleta Kominiarz', '04-06-1999', 'Oświęcim', 'Zimna 33',
                   '42-601', '345-235-678')
student3 = Student('Sławomira Pochopna', '20-08-1999', 'Milówka',
                   'Głośna 345', '30-776', '220-732-356')

# order1
# order2
# order3


# Zadanie 3
house = House('osiedle mieszkaniowe', 2, '250000', 'Czerwona 3', '1000')
flat = Flat('apartamentowiec', 3, '500000', 'Niebieska 3a/12', '10')

print(house)
print(flat)
