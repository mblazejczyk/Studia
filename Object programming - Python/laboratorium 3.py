#Mateusz Błażejczyk
#zad 2
class Vehicle:
    def __init__(self, brand, color, speed, fuel):
        self.brand = brand
        self.color = color
        self.speed = speed
        self.fuel = fuel

    def add_fuel(self, amount):
        self.fuel += amount

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5


class Car(Vehicle):
    def __init__(self, brand, color, speed, fuel, body_type, passengers_number):
        super().__init__(brand, color, speed, fuel)
        self.body_type = body_type
        self.passengers_number = passengers_number

    def inc_passengers(self):
        self.passengers_number += 1

    def dec_passengers(self):
        self.passengers_number -= 1


class Truck(Vehicle):
    def __init__(self, brand, color, speed, fuel, num_wheels, cargo_space, load):
        super().__init__(brand, color, speed, fuel)
        self.num_wheels = num_wheels
        self.cargo_space = cargo_space
        self.load = load

    def inc_load(self, amount):
        self.load += amount


car1 = Car('Toyota', 'Czerwony', 0, 20, 'sedan', 4)
truck1 = Truck('Volvo', 'Niebieski', 0, 50, 6, '10m3', 0)

print("Marka samochodu:", car1.brand)
print("Kolor samochodu:", car1.color)
print("Prędkość samochodu:", car1.speed)
print("Ilość paliwa w samochodzie:", car1.fuel)
print("Typ nadwozia samochodu:", car1.body_type)
print("Liczba pasażerów w samochodzie:", car1.passengers_number)

print("Marka ciężarówki:", truck1.brand)
print("Kolor ciężarówki:", truck1.color)
print("Prędkość ciężarówki:", truck1.speed)
print("Ilość paliwa w ciężarówce:", truck1.fuel)
print("Ilość kół w ciężarówce:", truck1.num_wheels)
print("Przestrzeń ładunkowa ciężarówki:", truck1.cargo_space)
print("Bieżący ładunek ciężarówki:", truck1.load)

car1.accelerate()
print("Prędkość samochodu po przyspieszeniu:", car1.speed)

truck1.add_fuel(10)
print("Ilość paliwa w ciężarówce po dolewie:", truck1.fuel)

car1.inc_passengers()
print("Liczba pasażerów w samochodzie po zwiększeniu:", car1.passengers_number)

truck1.inc_load(500)
print("Bieżący ładunek ciężarówki po zwiększeniu:", truck1.load)





#zad 3
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Zwierze daje głos")
        

class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def swim(self):
        print("Pływu pływu")
        
    def make_sound(self):
        print("Plum plum.")

        
class Mammal(Animal):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight


class Bird(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


class Cat(Mammal):
    def make_sound(self):
        print("Miau!")
    def cleaning(self):
        print("Kot się myje")


class Dog(Mammal):
    def make_sound(self):
        print("Hau!")
    def retrive(self):
        print("Retrive")


# przykładowe obiekty
cat1 = Cat("Garfield", 3, "pomaranczowy", 120)
cat2 = Cat("Felix", 5, "Biały", 200)
cat3 = Cat("Tom", 1, "Czarny", 220)
cat4 = Cat("Sylvester", 2, "Czarny w łatki", 190)
cat5 = Cat("Simba", 4, "Biało-pomarańczowy", 280)

dog1 = Dog("Fido", 7, "Czarny", 450)
dog2 = Dog("Rex", 2, "Biały", 550)
dog3 = Dog("Lucky", 4, "Bronzowy", 650)
dog4 = Dog("Buddy", 5, "Szary", 450)
dog5 = Dog("Max", 3, "Czarny", 550)

# lista i krotka obiektów
cat_list = [cat1, cat2, cat3, cat4, cat5]
dog_tuple = (dog1, dog2, dog3, dog4, dog5)

# wywołanie metod i wypisanie informacji
for cat in cat_list:
    cat.make_sound()
    print(f"{cat.name} ma {cat.age} lat.")

for dog in dog_tuple:
    dog.make_sound()
    print(f"{dog.name} ma {dog.age} lat.")





#zad 4
import math

class Shape:
    def __init__(self, color):
        self.color = color
    
    def __eq__(self, other):
        return isinstance(other, Shape)
    
    
class Triangle(Shape):
    def __init__(self, a=1, color = ""):
        super().__init__(color)
        self.a = a
    
    def calc_area(self):
        p = (math.pow(self.a, 2)*math.sqrt(3))/4
        return p
    
    def calc_parim(self):
        return self.a * 3
    
    def __ge__(self, other):
        return self.calc_area() >= other.calc_area()
    
    
class Circle(Shape):
    def __init__(self, radius=1, color = ""):
        super().__init__(color)
        self.radius = radius
    
    def calc_area(self):
        return math.pi * self.radius ** 2
    
    def calc_parim(self):
        return 2 * math.pi * self.radius
    
    def __truediv__(self, other):
        new_circle = Circle()
        new_circle.radius = self.radius / other.radius
        return new_circle
    
    
class Quadrangle(Shape):
    def __init__(self, a=1, color = ""):
        super().__init__(color)
        self.a = a
    
    def calc_area(self):
        pass
    
    def calc_parim(self):
        pass    
    def __add__(self, other):
        new_quad = Quadrangle()
        new_quad.a = self.a + other.a
        return new_quad
    
    
class Square(Quadrangle):
    def __init__(self, a=1, color = ""):
        super().__init__(a, color)
        
    def calc_area(self):
        return self.a ** 2
    
    def calc_parim(self):
        return 4 * self.a
    
    def __mul__(self, other):
        new_square = Square()
        new_square.a = self.a * other.a
        return new_square
    

class Rectangle(Quadrangle):
    def __init__(self, a=1, b=1, color = ""):
        super().__init__(a, color)
        self.b = b
    
    def calc_area(self):
        return self.a * self.b
    
    def calc_parim(self):
        return 2 * self.a + 2 * self.b
    
    def __sub__(self, other):
        new_rect = Rectangle()
        new_rect.a = max(self.a - other.a, 0)
        new_rect.b = max(self.b - other.b, 0)
        return new_rect
    

re = Rectangle(15, 5, "red")
print(re.calc_area())
print(re.calc_parim())

sq = Square(10, "orange")
print(sq.calc_area())
print(sq.calc_parim())

cir = Circle(5, "green")
print(cir.calc_parim())
print(cir.calc_area())

tr = Triangle(9, "purple")
print(tr.calc_area())
print(tr.calc_parim())

tr2 = Triangle(2, "red")
tr3 = tr >= tr2
print(tr3)

qu = Quadrangle(1, "red")
qu2 = Quadrangle(2, "red")
qu3 = qu + qu2
print(qu3.a)