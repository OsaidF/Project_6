from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator

# FIRST QUESTION
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")



student_01 = Student('Osaid', 20)
student_01.display()

# SECOND QUESTION
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def info(cls):
        print(f"Counter has been created {cls.count} times")

counter_01 = Counter()
counter_02 = Counter()
counter_03 = Counter()

counter_03.info()

# THIRD QUESTION
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} has started!")

ferrari_car = Car("Ferrari")
ferrari_car.start()

# FOURTH QUESTION
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
    
    def display(self):
        print(f"Name: {self.bank_name}")
    
    def change_bank_name(cls, name):
        cls.bank_name = name
    
new_bank = Bank('Bank of America') 
new_bank.display()
new_bank.change_bank_name('MCB Bank')
new_bank.display()


# FIFTH QUESTION
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtils.add(5, 3)
print("Result:", result)


# SIXTH QUESTION
class Logger:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created successfully!")
    def __del__(self):
        self
        print(f"{self.name} deleted successfully!")

log = Logger('logging object 01')
del log

# SEVENTH QUESTION
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    def print_details(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")


employee1 = Employee('Name', 30000, 165498746)
print(employee1.name)
print(employee1._salary)
# print(employee1.__ssn) # raises error


# EIGHTH QUESTION
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def details(self):
        print(f"Teacher name: {self.name}, Subject: {self.subject}")

teacher1 = Teacher("Ahmed", "Chemistry")
teacher1.details()


# NINTH QUESTION
class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass

class Rectangle(Shape):
    def area(self) -> None:
        print('Area: length X width')

class Circle(Shape):
    def area(self) -> None:
        print('Area: π X radius')

def area(shape: Shape):
    shape.area()    
shape1 = Rectangle()
area(shape1)


# TENTH QUESTION
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name}: Woof!")

dog1 = Dog("Tommy", "Labrador Retriever")
dog1.bark()


# ELEVENTH QUESTION
class Book:
    total_book = 0
    @classmethod
    def increment_book_count(cls):
        Book.total_book += 1

book1 = Book()
Book.increment_book_count()
book2 = Book()
Book.increment_book_count()
print(Book.total_book)

# TWELFTH QUESTION
class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(c):
        result = eval(f'({c} * 9/5) + 32')
        print(f"Result: {result}°F")

TemperatureConverter.celcius_to_fahrenheit(32)

# THIRTEENTH QUESTION
class Engine:
    def start(self):
        return "Engine starting"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print(f"Car starting... {self.engine.start()}...")
    
toyota = Car()
toyota.start()


# FOURTEENTH QUESTION
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employees(self, employee):
        self.employees.append(employee)

    def display_empolyees(self):
        print(self.employees)

employee_01 = Employee('Waqas')
employee_02 = Employee('Zakarya')
department = Department('Department of Education')

department.add_employees(employee_01.name)
department.add_employees(employee_02.name)
department.display_empolyees()


# FIFTEENTH QUESTION
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.show())


# SIXTEENTH QUESTION
def add_greeting(cls):
    cls.greeting = "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person1 = Person('Ahmed')
print(person1.greeting)


# EIGHTEENTH QUESTION
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

bread = Product(150)
print(bread.price)
bread.price = 160
print(bread.price)
del bread.price
# print(bread.price)


# NINETEENTH QUESTION
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, input):
        print(eval(f"{input} * {self.factor}"))

a = Multiplier(10)
a(2)


# TWENTEITH QUESTION
class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Insufficient age: {self.age} Age should be higher than 18.")

def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError(age)
        print(f"Apporopriate age: {age}")
    except Exception as e:
        print(e)

check_age(15)


# TWENTY FIRST QUESTION
class Countdown(Iterable):
    def __init__(self, count):
        self.data = count

    def __iter__(self):
        return MyIterator(self.data)
    
class MyIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        print("Called __next__")
        return value

count = Countdown([1, 2, 3])
for i in count:
    print(f"Count: {i}")