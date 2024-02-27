#zad 2
class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)


#zad 3
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"

class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class ConcreteFactoryA(AbstractFactory):
    def create_product(self):
        return ConcreteProductA()

class ConcreteFactoryB(AbstractFactory):
    def create_product(self):
        return ConcreteProductB()

def client_code(factory):
    product = factory.create_product()
    result = product.operation()
    print(result)

factory_a = ConcreteFactoryA()
client_code(factory_a)
factory_b = ConcreteFactoryB()
client_code(factory_b)



#zad 4
class Component:
    def operation(self):
        return "Component operation"

class Decorator:
    def __init__(self, component):
        self.component = component

    def operation(self):
        additional_functionality = "Decorator operation"
        return self.component.operation() + " " + additional_functionality

component = Component()
decorated_component = Decorator(component)
result = decorated_component.operation()
print(result)


#zad 5
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf operation"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite operation: {', '.join(results)}"

leaf1 = Leaf()
leaf2 = Leaf()

composite1 = Composite()
composite1.add(leaf1)
composite1.add(leaf2)

leaf3 = Leaf()
composite2 = Composite()
composite2.add(leaf3)
composite2.add(composite1)

result = composite2.operation()
print(result)



#zad 6
class RealClass:
    def operation(self):
        return "RealClass operation"

class ProxyClass:
    def __init__(self, real_object):
        self.real_object = real_object

    def operation(self):
        result = "ProxyClass pre-operation\n"
        result += self.real_object.operation()
        result += "\nProxyClass post-operation"
        return result

real_object = RealClass()
proxy = ProxyClass(real_object)

result = proxy.operation()
print(result)


#zad 7
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None

    def set_part_a(self, part_a):
        self.part_a = part_a

    def set_part_b(self, part_b):
        self.part_b = part_b

    def __str__(self):
        return f"Part A: {self.part_a}, Part B: {self.part_b}"

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_product(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.set_part_a("Part A")

    def build_part_b(self):
        self.product.set_part_b("Part B")

    def get_product(self):
        return self.product

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_product()
print(product)
