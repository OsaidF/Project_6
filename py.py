from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator

# FIRST QUESTION
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to 
# initialize these values via a constructor. Add a method display() that prints student details.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")



student_01 = Student('Osaid', 20)
student_01.display()

# SECOND QUESTION
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.
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
# Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} has started!")

ferrari_car = Car("Ferrari")
ferrari_car.start()

# FOURTH QUESTION
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method 
# change_bank_name(cls, name) that allows changing the bank name. Show that 
# it affects all instances.
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
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtils.add(5, 3)
print("Result:", result)


# SIXTH QUESTION
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) 
# and another message when it is destroyed (destructor).
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
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.
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
# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() 
# to call the base class constructor.
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
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().
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
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() 
# that prints a message including the dog's name.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name}: Woof!")

dog1 = Dog("Tommy", "Labrador Retriever")
dog1.bark()


# ELEVENTH QUESTION
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() 
# to increase the count when a new book is added.
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
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.
class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(c):
        result = eval(f'({c} * 9/5) + 32')
        print(f"Result: {result}°F")

TemperatureConverter.celcius_to_fahrenheit(32)

# THIRTEENTH QUESTION
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to 
# the Car class during initialization. Access a method of the Engine class via the Car class.
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
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department 
# object store a reference to an Employee object that exists independently of it.
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
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.
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
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello(). '''
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()


# SEVENTEENTH QUESTION
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class Person.
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
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, 
# @price.setter to update it, and @price.deleter to delete it.
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
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() 
# method that multiplies an input by the factor. Test it with callable() and by 
# calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, input):
        print(eval(f"{input} * {self.factor}"))

a = Multiplier(10)
a(2)


# TWENTEITH QUESTION
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that 
# raises this exception if age < 18. Handle it with try...except.
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
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() 
# to make the object iterable in a for-loop, counting down to 0.
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