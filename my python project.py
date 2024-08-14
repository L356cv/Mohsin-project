#practice 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Alice", 30)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
#practice 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}!")
person1 = Person("Alice", 30)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
person1.greet()
#practice 3
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_details(self):
        print(f"Car Details:\n  Make: {self.make}\n  Model: {self.model}\n  Year: {self.year}")
car1 = Car("Toyota", "Camry", 2022)
car1.car_details()
#practice 4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14159 * self.radius ** 2
radius = 5
circle = Circle(radius)
area = circle.compute_area()
print(f"Area of the circle with radius {radius} is: {area}")
#practice 5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
rect = Rectangle(5, 3)
print("Area:", rect.area())         
print("Perimeter:", rect.perimeter())
#practice 6
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()

print("Dog says:", dog.speak()) 
print("Cat says:", cat.speak()) 
#ptactice 7
class Shape:
        def area(self):
            raise NotImplementedError("Subclasses must implement this method")

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
square = Square(4)
triangle = Triangle(3, 5)

print("Square area:", square.area())    
print("Triangle area:", triangle.area())  
#practice 8
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self.salary})"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager(Name: {self.name}, Salary: {self.salary}, Department: {self.department})"
employee = Employee("John Doe", 50000)
manager = Manager("Jane Smith", 80000, "IT")

print(employee)  
print(manager)   
#practice 9
class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclasses must implement this method")

class Bike(Vehicle):
    def drive(self):
        return "Riding the bike!"

class Truck(Vehicle):
    def drive(self):
        return "Driving the truck!"
bike = Bike()
truck = Truck()

print(bike.drive())  
print(truck.drive())  
#practice 10
class Bird:
    def fly(self):
        return "This bird can fly."

class Eagle(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly."
bird = Bird()
eagle = Eagle()
penguin = Penguin()

print(bird.fly())    
print(eagle.fly())   
print(penguin.fly()) 
#practice 11
class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance is {self.__balance}."
        elif amount > self.__balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return self.__balance
account = Account(100)
print(account.deposit(50))  
print(account.withdraw(30))  
print(account.withdraw(200))
print(account.get_balance()) 
#practice 12
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Number of pages must be positive.")
book = Book("1984", "George Orwell", 328)
print(book.get_title())
print(book.get_author()) 
print(book.get_pages())  

book.set_title("Animal Farm")
book.set_author("George Orwell")
book.set_pages(112)
print(book.get_title())  
print(book.get_author()) 
print(book.get_pages())  
#practice 13
class Laptop:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def apply_discount(self, discount_percentage):
        if 0 < discount_percentage < 100:
            discount_amount = (discount_percentage / 100) * self.__price
            self.__price -= discount_amount
        else:
            raise ValueError("Discount percentage must be between 0 and 100.")

    def display_details(self):
        return f"Laptop Details:\nBrand: {self.__brand}\nModel: {self.__model}\nPrice: ${self.__price:.2f}"
laptop = Laptop("Dell", "XPS 15", 1500.00)
print(laptop.display_details())

laptop.apply_discount(10)
print(laptop.display_details())
#practice 14
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance is ${self.__balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__balance}."
        elif amount > self.__balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Current balance is ${self.__balance}."
account = BankAccount("123456789", 500)
print(account.check_balance()) 

print(account.deposit(150))    
print(account.withdraw(100))   
print(account.withdraw(600))

print(account.check_balance())
#practice 15
class Student:
    def __init__(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive number.")
    def display_details(self):
        return (f"Student Details:\n"
                f"Name: {self.__name}\n"
                f"Grade: {self.__grade}\n"
                f"Age: {self.__age}")
student = Student("Alice", "A", 20)
print(student.display_details())

student.set_name("Bob")
student.set_grade("B")
student.set_age(21)
print(student.display_details())
#practice 16
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
        

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            return f"Book '{book.title}' added to the library."
        else:
            return "Only instances of Book can be added."

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Book '{title}' removed from the library."
        return f"No book with title '{title}' found."

    def list_books(self):
        if self.books:
            return "\n".join([str(book) for book in self.books])
        else:
            return "No books in the library."
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

library = Library("City Library")
print(library.add_book(book1)) 
print(library.add_book(book2))  
print(library.list_books())

print(library.remove_book("1984"))  
print(library.list_books())
#practice 17
class Student:
    def __init__(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive number.")
    def display_details(self):
        return (f"Student Details:\n"
                f"Name: {self.__name}\n"
                f"Grade: {self.__grade}\n"
                f"Age: {self.__age}")

    def __repr__(self):
        return f"Student(name='{self.__name}', grade='{self.__grade}', age={self.__age})"
        
        
        
class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            return f"Student '{student.get_name()}' added to the school."
        else:
            return "Only instances of Student can be added."

    def remove_student(self, name):
        for student in self.students:
            if student.get_name() == name:
                self.students.remove(student)
                return f"Student '{name}' removed from the school."
        return f"No student with name '{name}' found."

    def list_students(self):
        if self.students:
            return "\n".join([str(student) for student in self.students])
        else:
            return "No students in the school."
student1 = Student("Alice", "A", 20)
student2 = Student("Bob", "B", 21)

school = School("Greenwood High")
print(school.add_student(student1))  
print(school.add_student(student2)) 
print(school.list_students())

print(school.remove_student("Alice")) 
print(school.list_students())
#practice 18
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        if isinstance(person, Person):
            self.members.append(person)
            return f"Member '{person.name}' added to the team."
        else:
            return "Only instances of Person can be added."

    def remove_member(self, name):
        for person in self.members:
            if person.name == name:
                self.members.remove(person)
                return f"Member '{name}' removed from the team."
        return f"No member with name '{name}' found."

    def list_members(self):
        if self.members:
            return "\n".join([str(person) for person in self.members])
        else:
            return "No members in the team."
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

team = Team("Development Team")
print(team.add_member(person1))  
print(team.add_member(person2)) 
print(team.list_members())

print(team.remove_member("Alice"))  
print(team.list_members())
#practice 19
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"Employee(name='{self.name}', position='{self.position}')"
class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            return f"Employee '{employee.name}' added to the company."
        else:
            return "Only instances of Employee can be added."

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return f"Employee '{name}' removed from the company."
        return f"No employee with name '{name}' found."

    def list_employees(self):
        if self.employees:
            return "\n".join([str(employee) for employee in self.employees])
        else:
            return "No employees in the company."

employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Manager")

company = Company("Tech Innovations")
print(company.add_employee(employee1)) 
print(company.add_employee(employee2))  
print(company.list_employees())

print(company.remove_employee("Alice"))
print(company.list_employees())
#practice 20
class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def __repr__(self):
        return f"Animal(species='{self.species}', name='{self.name}')"
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            return f"Animal '{animal.name}' added to the zoo."
        else:
            return "Only instances of Animal can be added."

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                return f"Animal '{name}' removed from the zoo."
        return f"No animal with name '{name}' found."

    def list_animals(self):
        if self.animals:
            return "\n".join([str(animal) for animal in self.animals])
        else:
            return "No animals in the zoo."
animal1 = Animal("Lion", "Leo")
animal2 = Animal("Elephant", "Ella")

zoo = Zoo("Safari Park")
print(zoo.add_animal(animal1)) 
print(zoo.add_animal(animal2))  
print(zoo.list_animals())

print(zoo.remove_animal("Leo"))
print(zoo.list_animals())
#practice 21
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
            return "Content successfully written to the file."
        except IOError as e:
            return f"Error writing to file: {e}"

    def read_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except IOError as e:
            return f"Error reading from file: {e}"
file_manager = FileManager("example.txt")

write_result = file_manager.write_to_file("Hello, world!")
print(write_result)  
read_result = file_manager.read_from_file()
print(read_result)
#practice 22
import datetime

class Log:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def write_error(self, message):
        try:
            with open(self.log_file_path, 'a') as log_file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp} - ERROR: {message}\n")
            return "Error message successfully written to the log file."
        except IOError as e:
            return f"Error writing to log file: {e}"
log = Log("error.log")
result = log.write_error("This is a test error message.")
print(result)  
#practice 23
class Config:
    def __init__(self, filename):
        self.settings = {}
        self._load_settings(filename)

    def _load_settings(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split('=', 1)
                self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def get_int(self, key, default=0):
        return int(self.settings.get(key, default))

    def get_bool(self, key, default=False):
        return self.settings.get(key, str(default)).lower() in ('true', '1', 'yes')


config = Config('config.txt')
host = config.get('host')
port = config.get_int('port')
debug = config.get_bool('debug')
#practice 24
import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None
        self._connect()

    def _connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print("Connection to database established successfully.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

db = Database("example.db")
db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
db.execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))


result = db.execute_query("SELECT * FROM users")
print(result) 
db.close()
#practice 25
import os

class Report:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def _load_data(self):
        
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")
            
            with open(self.file_path, 'r') as file:
                self.data = file.readlines()
              
                print(f"Data successfully loaded from '{self.file_path}'.")
        
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(f"Error reading file '{self.file_path}': {e}")

    def generate_report(self):
       
        self._load_data()
        
        if not self.data:
            print("No data to generate the report.")
            return
        
     
        report = "Report Generated:\n\n"
        report += "".join(self.data) 
        
        print(report)


report = Report("data.txt")
report.generate_report()
#practice 26
class Ticket:
    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price

    def display_details(self):
        
        return (f"Movie: {self.movie_name}\n"
                f"Seat Number: {self.seat_number}\n"
                f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percentage):
       
        if not (0 <= discount_percentage <= 100):
            return "Invalid discount percentage. Must be between 0 and 100."
        
        discount_amount = (self.price * discount_percentage) / 100
        self.price -= discount_amount
        return f"Discount applied. New price: ${self.price:.2f}"

ticket = Ticket("Inception", "A12", 15.00)


print(ticket.display_details())
print(ticket.apply_discount(10)) 
print(ticket.display_details())
#practice 27
class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} x {self.quantity}"

    def total_price(self):
        return self.price * self.quantity
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to the cart.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item.name} from the cart.")
                break
        else:
            print(f"Item {item_name} not found in the cart.")

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(f" - {item}")
            print(f"Total: ${self.get_total():.2f}")

    def get_total(self):
        return sum(item.total_price() for item in self.items)

apple = Item("Apple", 0.99, 3)
banana = Item("Banana", 0.59, 2)
milk = Item("Milk", 2.99, 1)


cart = ShoppingCart()
cart.add_item(apple)
cart.add_item(banana)
cart.add_item(milk)


cart.display_cart()

cart.remove_item("Banana")

cart.display_cart()
#practice 28
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price:.2f})"

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        if isinstance(item, Item):
            self.menu.append(item)
            return f"Added {item.name} to the menu."
        else:
            return "Only instances of Item can be added to the menu."

    def remove_item(self, item_name):
        for item in self.menu:
            if item.name == item_name:
                self.menu.remove(item)
                return f"Removed {item_name} from the menu."
        return f"Item '{item_name}' not found on the menu."

    def display_menu(self): 
        if not self.menu:
            return "The menu is currently empty."
        
        menu_list = "\n".join([str(item) for item in self.menu])
        return f"Menu for {self.name}:\n{menu_list}"

# Example 
item1 = Item("Burger", 8.99)
item2 = Item("Pizza", 12.99)

restaurant = Restaurant("The Gourmet Spot")
print(restaurant.add_item(item1)) 
print(restaurant.add_item(item2)) 
print(restaurant.display_menu())
print(restaurant.remove_item("Pizza"))
print(restaurant.display_menu())
#practice 29
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []

    def add_passenger(self, person):
        
        if isinstance(person, Person):
            self.passengers.append(person)
            return f"Added {person.name} to the flight."
        else:
            return "Only instances of Person can be added as passengers."

    def remove_passenger(self, name):
       
        for person in self.passengers:
            if person.name == name:
                self.passengers.remove(person)
                return f"Removed {name} from the flight."
        return f"Passenger '{name}' not found on the flight."

    def display_passengers(self):
        
        if not self.passengers:
            return "No passengers on this flight."
        
        passenger_list = "\n".join([str(person) for person in self.passengers])
        return f"Passengers on Flight {self.flight_number} to {self.destination}:\n{passenger_list}"
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

flight = Flight("AB123", "New York")
print(flight.add_passenger(person1)) 
print(flight.add_passenger(person2)) 
print(flight.display_passengers())
print(flight.remove_passenger("Bob"))  
print(flight.display_passengers())
#practice 30
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False

    def __repr__(self):
        status = "Occupied" if self.is_occupied else "Available"
        return f"Room(room_number={self.room_number}, status={status})"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        
        if isinstance(room, Room):
            self.rooms.append(room)
            return f"Room {room.room_number} added to the hotel."
        else:
            return "Only instances of Room can be added."

    def book_room(self, room_number):
        
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_occupied:
                    return f"Room {room_number} is already occupied."
                else:
                    room.is_occupied = True
                    return f"Room {room_number} has been booked."
        return f"Room {room_number} not found."

    def check_out_room(self, room_number):
        
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_occupied:
                    return f"Room {room_number} is not occupied."
                else:
                    room.is_occupied = False
                    return f"Room {room_number} has been checked out."
        return f"Room {room_number} not found."

    def display_rooms(self):
       
        if not self.rooms:
            return "No rooms available in the hotel."
        
        room_list = "\n".join([str(room) for room in self.rooms])
        return f"Rooms in Hotel {self.name}:\n{room_list}"

room1 = Room(101)
room2 = Room(102)
room3 = Room(103)

hotel = Hotel("Grand Palace")
print(hotel.add_room(room1)) 
print(hotel.add_room(room2))  
print(hotel.add_room(room3))  
print(hotel.book_room(102))  
print(hotel.display_rooms())

print(hotel.check_out_room(102))  
print(hotel.display_rooms())
#practice 36
import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")

        self.counter = 0

     
        self.label = tk.Label(root, text=str(self.counter), font=('Helvetica', 48))
        self.label.pack(pady=20)

       
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        self.increment_button = tk.Button(self.button_frame, text="Increment", command=self.increment, font=('Helvetica', 14))
        self.increment_button.pack(side="left", padx=10)

       
        self.decrement_button = tk.Button(self.button_frame, text="Decrement", command=self.decrement, font=('Helvetica', 14))
        self.decrement_button.pack(side="left", padx=10)

    def increment(self):
        self.counter += 1
        self.update_label()

    def decrement(self):
        self.counter -= 1
        self.update_label()

    def update_label(self):
        self.label.config(text=str(self.counter))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
#ptactice 37
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
       
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
   
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
    def add_task(self):
        
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def remove_task(self):
        
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
#practice 38
import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""
        
     
        self.entry = ttk.Entry(root, font=('Helvetica', 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        
        button_texts = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        
        row_val = 1
        col_val = 0
        for text in button_texts:
            self.create_button(text).grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

       
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            root.grid_rowconfigure(i+1, weight=1)
    
    def create_button(self, text):
        return ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t), style='TButton')

    def on_button_click(self, char):
        if char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif char == "C":
            self.expression = ""
        else:
            self.expression += str(char)
        self.update_entry()
    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 14))
    app = CalculatorApp(root)
    root.mainloop()
#practice 39
import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.username_label = tk.Label(root, text="Username:", font=('Helvetica', 14))
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.username_entry = tk.Entry(root, font=('Helvetica', 14))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.password_label = tk.Label(root, text="Password:", font=('Helvetica', 14))
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.password_entry = tk.Entry(root, font=('Helvetica', 14), show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        
        self.login_button = tk.Button(root, text="Login", font=('Helvetica', 14), command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.validate_login(username, password):
            messagebox.showinfo("Login Success", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def validate_login(self, username, password):
       
        return username == "user" and password == "pass"

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
#practice 40

import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.city_label = tk.Label(root, text="City:", font=('Helvetica', 14))
        self.city_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.city_entry = tk.Entry(root, font=('Helvetica', 14))
        self.city_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

      
        self.search_button = tk.Button(root, text="Search", font=('Helvetica', 14), command=self.search_weather)
        self.search_button.grid(row=1, column=0, columnspan=2, pady=20)

     
        self.weather_info = tk.Label(root, text="", font=('Helvetica', 14))
        self.weather_info.grid(row=2, column=0, columnspan=2, pady=10)

    def search_weather(self):
        city = self.city_entry.get()
        
        if city:
            weather = self.get_weather(city)
            if weather:
                self.weather_info.config(text=f"City: {city}\nTemperature: {weather['temperature']}°C\nCondition: {weather['condition']}")
            else:
                messagebox.showerror("Error", "City not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a city name.")

    def get_weather(self, city):
       
        weather_data = {
            "New York": {"temperature": 25, "condition": "Sunny"},
            "London": {"temperature": 18, "condition": "Cloudy"},
            "Paris": {"temperature": 22, "condition": "Partly Cloudy"},
            "Tokyo": {"temperature": 30, "condition": "Hot"}
        }
        
        return weather_data.get(city)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
