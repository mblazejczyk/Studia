#Mateusz Błażejczyk
#zad 2
class Counter:
    def __init__(self):
        self.count = 0

    def inc_nr(self):
        self.count += 1

    def dec_nr(self):
        if self.count > 0:
            self.count -= 1

    def check_nr(self):
        return self.count

counter = Counter()
counter.inc_nr()
print(counter.check_nr())





#zad 3
class Rectangle:
    def __init__(self):
        self.a = 0
        self.b = 0

    def read_data(self, a, b):
        self.a = a
        self.b = b

    def calc_parim(self):
        return 2 * self.a + 2 * self.b

    def calc_area(self):
        return self.a * self.b

prostokat = Rectangle()
prostokat.read_data(2, 5)
print(prostokat.calc_area())
print(prostokat.calc_parim())





#zad 4
class Moneybox:
    def __init__(self):
        self.money = 0

    def insert_money(self, amount):
        self.money += amount

    def break_moneybox(self):
        total_money = self.money
        self.money = 0
        return total_money


Skarbonka = Moneybox()
Skarbonka.insert_money(100)
Skarbonka.insert_money(150)
print(Skarbonka.break_moneybox())
print(Skarbonka.break_moneybox())





#zad 5
class Car:
    def __init__(self, model, brand, year, speed):
        self.model = model
        self.brand = brand
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

auto = Car('e36', 'BMW', 1990, 0)
auto.accelerate()
print(auto.speed)
auto.accelerate()
print(auto.speed)
auto.accelerate()
print(auto.speed)
auto.brake()
print(auto.speed)





#zad 6
class Book:
    def __init__(self, author='', title='', year=0, price=0):
        self.author = author
        self.title = title
        self.year = year
        self.price = price

    def input_book(self):
        self.author = input('Enter author: ')
        self.title = input('Enter title: ')
        self.year = input('Enter year: ')
        self.price = input('Enter price: ')

    def print_book(self):
        print(f'Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}')

    def discount(self):
        self.price *= 0.8

ksiazki = []
imiona = ['Adam', 'Aleksander', 'Anna', 'Bartosz', 'Dariusz', 'Ewa', 'Karolina', 'Krystyna', 'Piotr', 'Tomasz', 'Zofia']
tytuly = ['Zakleta ksiega', 'Ostatni bastion', 'Nastepny pokoj', 'Ostatnia gra', 'Pierwszy mecz swiata', 'Ksiega rekordow', 'Jan i przygody', 'Lowca skarbow', 'Kolejny znak', 'Tajemnica marzen']
for i in range(10):
    ksiazka = Book(imiona[i], tytuly[i], 2022, 25)
    ksiazki.append(ksiazka)

for i in range(len(ksiazki)):
    ksiazki[i].print_book()






#zad 7
class Dog:
    def __init__(self, name="", age=0, weight=0, breed=""):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed

    def display_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Breed: {self.breed}")

    def bark(self):
        print("Hau!")


psy = []
psy.append(Dog("Barczus", 5, 10, "Jamnik"))
psy.append(Dog("Aleks", 3, 7, "Labrador"))
psy.append(Dog("Chmurka", 2, 5, "Chihuahua"))

psy_krotka = tuple(psy)

klon = psy_krotka[1]

klon.display_data()
klon.bark()
