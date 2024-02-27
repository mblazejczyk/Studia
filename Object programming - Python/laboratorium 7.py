#zad 2
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)


class Observer:
    def update(self, event):
        pass



class EmailNotifier(Observer):
    def update(self, event):
        print("Wysyłanie powiadomienia email:", event)


class SMSNotifier(Observer):
    def update(self, event):
        print("Wysyłanie powiadomienia SMS:", event)



class Event:
    def __init__(self, name):
        self.name = name



subject = Subject()

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

subject.attach(email_notifier)
subject.attach(sms_notifier)

event = Event("Nowe zdarzenie")
subject.notify(event)

subject.detach(sms_notifier)

event = Event("Inne zdarzenie")
subject.notify(event)




#zad 3
class Strategy:
    def execute(self, data):
        pass


class StrategyA(Strategy):
    def execute(self, data):
        print("Wykonuję strategię A na danych:", data)


class StrategyB(Strategy):
    def execute(self, data):
        print("Wykonuję strategię B na danych:", data)


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        self.strategy.execute(data)



strategy_a = StrategyA()
strategy_b = StrategyB()

context = Context(strategy_a)
context.execute_strategy("Dane 1")

context.set_strategy(strategy_b)
context.execute_strategy("Dane 2")




#zad 4
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass


class ConcreteClassA(AbstractClass):
    def step_one(self):
        print("Krok 1 w ConcreteClassA")

    def step_two(self):
        print("Krok 2 w ConcreteClassA")

    def step_three(self):
        print("Krok 3 w ConcreteClassA")


class ConcreteClassB(AbstractClass):
    def step_one(self):
        print("Krok 1 w ConcreteClassB")

    def step_two(self):
        print("Krok 2 w ConcreteClassB")

    def step_three(self):
        print("Krok 3 w ConcreteClassB")



concrete_class_a = ConcreteClassA()
concrete_class_a.template_method()

concrete_class_b = ConcreteClassB()
concrete_class_b.template_method()




#zad 5
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light:
    def turn_on(self):
        print("Włączono światło.")

    def turn_off(self):
        print("Wyłączono światło.")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class RemoteControl:
    def __init__(self):
        self.commands = []
        self.undo_command = None

    def set_command(self, command):
        self.commands.append(command)

    def press_button(self, button):
        if button < len(self.commands):
            self.commands[button].execute()
            self.undo_command = self.commands[button]

    def undo_button(self):
        if self.undo_command:
            self.undo_command.undo()


light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)

remote_control = RemoteControl()
remote_control.set_command(light_on_command)
remote_control.set_command(light_off_command)

remote_control.press_button(0)  
remote_control.press_button(1) 

remote_control.undo_button()
remote_control.undo_button()    


#zad 6
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass


class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("ConcreteHandler1 obsługuje żądanie:", request)
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("ConcreteHandler2 obsługuje żądanie:", request)
        elif self._successor is not None:
            self._successor.handle_request(request)


class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == 'C':
            print("ConcreteHandler3 obsługuje żądanie:", request)
        elif self._successor is not None:
            self._successor.handle_request(request)


handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()
handler3 = ConcreteHandler3()

handler1._successor = handler2
handler2._successor = handler3

handler1.handle_request('A')
handler1.handle_request('B')
handler1.handle_request('C')
handler1.handle_request('D')