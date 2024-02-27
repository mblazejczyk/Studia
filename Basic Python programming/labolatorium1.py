#Mateusz Błażejczyk
#zadanie 1 i 2
#Moj pierwszy komentarz liniowy
'''To jest komentarz
Blokowy'''



#zadanie 3
a = 5
b = 14
c = 26

print(a + b + c)
print(a * b * c)
print(c - b - a)
print(c / b)



#zadanie 4
a = 5
b = 14
c = 26

d = a%b%c
print(d)



#zadanie 5
a = float(input("Podaj szerszy bok: "))
b = float(input("Podaj krótszy bok: "))

print("%.2f" % (a*b))



#zadanie 6
import math
a = float(input("Podaj promień: "))

obj = (4/3)*math.pi*pow(a, 3)
pol = 4*math.pi*pow(a, 2)

print("Objętość wynosi: " + ("%.2f" % obj))
print("Natomiast pole wynosi: " + ("%.2f" % pol))



#zadanie 7
a = float(input("Podaj stopnie celstiusza: "))
wyn = 32 + (9.0*a)/5
print("to jest w Fahrenheitach: " + str(wyn))



#zadanie 8
a = int(input("Podaj dowolną liczbę: "))

if(a > 100):
    print("Podana liczba jest większa od 100")
if(a < 0):
    print("Podana liczba jest mniejsza od 0")
if(a > 0 and a < 100):
    print("Podana liczba jest w przedziale między 0 a 100")



#zadanie 9
while True:
    a = input("Podaj literę: ")
    if(a == 'c'):
        print("Podana litera jest odpowiednia")
        break
    else:
        print("Spróbuj ponownie")