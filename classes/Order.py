import classes.Student as Student
import classes.Employee as Employee


class Order(Student, Employee):
    def __init__(self, first_name, last_name, name, marks, books, order_date):
        super().__init__(first_name, last_name, name, marks)
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return (f'Zamówenie złożone dla {self.name} przez {self.first_name}' +
                f' {self.last_name} na książki: {self._books}, dnia' +
                f' {self._order_date}')
