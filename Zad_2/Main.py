from Library import Library
from Employee import Employee
from Student import Student
from Book import Book
from Order import Order

# Libraries
library1 = Library("Warsaw", "Main Street 1", "00-001", "8:00-18:00", "123456789")
library2 = Library("Krakow", "Old Town 5", "30-001", "9:00-17:00", "987654321")

# Employees
employee1 = Employee("Anna", "Nowak", "2020-01-10", "1990-05-12",
                     "Warsaw", "Green St 3", "00-002", "111222333")
employee2 = Employee("Piotr", "Kowalski", "2019-03-15", "1988-08-20",
                     "Krakow", "Blue St 7", "30-002", "444555666")
employee3 = Employee("Maria", "Wisniewska", "2021-06-01", "1995-02-10",
                     "Warsaw", "Red St 9", "00-003", "777888999")

# Students
student1 = Student("Ahmed")
student2 = Student("John")
student3 = Student("Emily")

# Books
book1 = Book(library1, "2010", "George", "Orwell", 328)
book2 = Book(library1, "1997", "J.K.", "Rowling", 223)
book3 = Book(library2, "1869", "Leo", "Tolstoy", 1225)
book4 = Book(library2, "1925", "F. Scott", "Fitzgerald", 180)
book5 = Book(library1, "1954", "William", "Golding", 224)

# Orders
order1 = Order(employee1, student1, [book1, book2], "2024-05-01")
order2 = Order(employee2, student2, [book3, book4, book5], "2024-05-02")

# Print orders
print(order1)
print()
print(order2)
