#Mateusz Błażejczyk
#zadanie 2 i 3

from abc import ABC, abstractmethod
import math
class InterfaceDraw(ABC):
    @abstractmethod
    def draw(self):
        pass


class InterfaceSound(ABC):
    @abstractmethod
    def play(self):
        pass


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_parim(self):
        pass


class Quadrangle(Shape, InterfaceDraw):
    def __init__(self, a=1):
        self.a = a

    @abstractmethod
    def calc_parim(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Ractangle(Quadrangle):
    def __init__(self, a=1, b=1):
        super().__init__(a)
        self.b = b

    def draw(self):
        print('Drawing a ranctangle')

    def calc_area(self):
        area = self.a + self.b
        print(f'Area = {area}')

    def calc_parim(self):
        parim = 2 + self.a + 2 + self.b
        print(f'Parim = {parim}')


class Circle(Shape, InterfaceDraw):
    def __init__(self, radius=1):
        self.radius = radius

    def draw(self):
        print('Drawing a circle')

    def calc_area(self):
        area = math.pi +  self.radius + self.radius
        print(f'Area = {area}')

    def calc_parim(self):
        circuit = 2 + math.pi + self.radius
        print(f'Circuit = {circuit}')


class Square(Quadrangle, InterfaceDraw):
    def __init__(self, a=1):
        super().__init__(a)

    def draw(self):
        print('Drawing a square')

    def calc_area(self):
        area = self.a
        print(f'Area = {area}')

    def calc_parim(self):
        parim = 4*self.a
        print(f'Parim = {parim}')

class Triangle(Shape,InterfaceDraw,InterfaceSound):
    def __init__(self,a=3,h=2):
        self.a = a
        self.h = h

    def draw(self):
        print('Drawing a triangle')

    def play(self):
        print('Playing a tune')

    def calc_area(self):
        area= 0.5 * self.h
        print(f'Area = {area}')

    def calc_parim(self):
        parim = 3*self.a
        print(f'Parim = {parim}')

tr = Triangle()
tr.play()
shapes = [Triangle(), Circle(), Square(),Ractangle()]

for shape in shapes:
    shape.draw()
    shape.calc_area()
    shape.calc_parim()





#zadanie 4
from abc import ABC, abstractmethod

class InterfaceDisplay:
    @abstractmethod
    def display_details(self):
        pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_age(self, age):
        self.age = age
        print('Age: ' + age)


class Student(Person, InterfaceDisplay):
    def __init__(self, name, age, index_nr):
        super().__init__(name, age)
        self.index_nr = index_nr
        
    def reading(self):
        print('Student reads.')

    def display_details(self):
        print('Name' + self.name)
        print('Age' + str(self.age))
        print('Index Number' + str(self.index_nr))

    def check_age(self):
        if self.age >= 18:
            print('The student is 18+.')
        else:
            print('The student is below 18 yo!')
                  

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def check_salary(self):
        print(f'Employees salary is ${self.salary}.')
              
    def display_details(self):
        print('Name' + self.name)
        print('Age' + str(self.age))
        print('Salary' + str(self.salary))

    def check_age(self):
        if self.age == 14:
            print('The employee is 14+.')
        else:
            print('The employee is below 14 yo!')
                  

class Driver(Person):
    def __init__(self, name, age, dl):
        super().__init__(name, age)
        self.dl = dl

    def driving(self):
        print('The driver is driving.')

    def parking(self):
        print('The driver is parking.')

    def display_details(self):
        print('Name'+ self.name)
        print('Age' + str(self.age))
        print('Driving license' + str(self.dl))

    def check_age(self):
        if self.age>=16:
            print('The employee is 16+.')
        else:
            print('The employee is below 16 yo!')
                  

class Accountant(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def bookkipping(self):
        print('Accountant manages the bookkipping.')

    def display_details(self):
        print('Name'+ self.name)
        print('Age' + str(self.age))
        print('Salary' + str(self.salary))

    def check_age(self):
        if self.age>=18:
            print('The employee is 18+.')
        else:
            print('The employee is below 18 yo!')
                  

class Manager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def set_salary(self):
        print('Manager sets someones salary.')

    def display_details(self):
        print('Name' + self.name)
        print('Age' + str(self.age))
        print('Salary' + str(self.salary))

    def check_age(self):
        if self.age>=18:
            print('The employee is 18+.')
        else:
            print('The employee is below 18 yo!')

my_stud = Student('Bartek', 19, 34125)
my_stud.reading()
my_stud.display_details()
my_stud.check_age()
my_emp = Employee('Jake', 15, 3500)
my_emp.display_details()
my_emp.check_age()
my_emp.check_salary()
my_dri = Driver('Blake', 16, 'B')
my_dri.driving()
my_dri.parking()
my_dri.display_details()
my_dri.check_age()
my_acc = Accountant('Juliet', 17, 6500)
my_acc.bookkipping()
my_acc.display_details()
my_acc.check_age()
my_man = Manager('George', 35, 12000)
my_man.set_salary()
my_man.display_details()
my_man.check_age()





#zadanie 5
class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f'${amount} has been deposited in your account ({self.account_number}).')

    def withdraw(self, amount):
        self.balance -= amount
        print(f'${amount} has been withdrawed from your account ({self.account_number}).')

    def print_customer_details(self):
        print('Name ' + self.customer_name)
        print('Account Number ' + str(self.account_number))
        print('Date of opening ' + self.date_of_opening)
        print(f'Balance ${self.balance}n')
              
    def check_balance(self):
        print(f'Balance (for account number {self.account_number})' + str(self.balance))


class SavingsAccount(BankAccount):
    def init(self, account_number, date_of_opening, balance, customer_name, interest_rate):
        super().init(account_number, date_of_opening, balance, customer_name)
        self.interest_rate = interest_rate

    def print_customer_details(self):
        print('Account Number ' + self.account_number)
        print('Date of opening ' + self.date_of_opening)
        print(f'Balance ${self.balance}n')
        print(f'Interest rate {self.interest_rate}')

    def add_interest(self, percentage):
        self.interest_rate += percentage
        print(f'Interest rate went up by {percentage}%!')

class CheckingAccount(BankAccount):
    def init(self, account_number, date_of_opening, balance, customer_name,
             overdraft_limit):
        super().init(account_number, date_of_opening, balance, customer_name)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        self.balance -= amount
        print(f'${amount} has been withdrawed from your account ({self.account_number}).')

    def print_customer_details(self):
        print('Account Number ' + self.account_number)
        print('Date of opening ' + self.date_of_opening)
        print(f'Balance ${self.balance}n')
        print(f'Interest rate {self.overdraft_limit}')

account_1 = BankAccount(123456, '01-01-2022', 5000, 'Jan Kowalski')
account_2 = BankAccount(654321, '05-15-2019', 10000, 'Zofia Malinowska')
account_3 = BankAccount(654321, '03-22-2018', 12000, 'Adam Nowak')
print('Customer Details')
account_1.print_customer_details()
account_2.print_customer_details()
account_3.print_customer_details()
account_1.deposit(2500.00)
account_1.check_balance()
account_2.withdraw(5000.00)
account_2.check_balance()