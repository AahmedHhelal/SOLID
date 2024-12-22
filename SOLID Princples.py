# 1. Single Responsibility Principle (SRP)
# A class should have only one reason to change, meaning it should have only one job or responsibility.

class Report:
    def generate_report(self):
        return "Report content"

class ReportPrinter:
    def print_report(self, report):
        print(report)

# Usage
report = Report()
report_content = report.generate_report()
printer = ReportPrinter()
printer.print_report(report_content)
print('####################################################################################################################################################')



# 2. Open/Closed Principle (OCP)
# Software entities should be open for extension but closed for modification. This means you should be able to add new functionality without changing existing code.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(shape.area())
print('####################################################################################################################################################')



# 3. Liskov Substitution Principle (LSP)
# Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

# Usage
def make_bird_fly(bird: Bird):
    print(bird.fly())

sparrow = Sparrow()
make_bird_fly(sparrow)

ostrich = Ostrich()
print('####################################################################################################################################################')
# make_bird_fly(ostrich)  # This would raise an exception


# 4. Interface Segregation Principle (ISP)
# Clients should not be forced to depend on interfaces they do not use. This means creating smaller, more specific interfaces rather than a large, general-purpose one.

class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

# Usage
mfd = MultiFunctionDevice()
mfd.print()
mfd.scan()
print('####################################################################################################################################################')



# 5. Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL")

class UserService:
    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user):
        self.database.save(user)

# Usage
db = MySQLDatabase()
user_service = UserService(db)
user_service.save_user("John Doe")
print('####################################################################################################################################################')


# ##############################################################################################################################################################


