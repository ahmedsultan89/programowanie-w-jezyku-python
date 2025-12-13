from Employee import Employee
from Student import Student
from Book import Book


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list = "\n".join(str(book) for book in self.books)
        return (
            f"Order date: {self.order_date}\n"
            f"Student: {self.student.name}\n"
            f"Handled by: {self.employee.first_name} "
            f"{self.employee.last_name}\n"
            f"Books:\n{books_list}"
        )
