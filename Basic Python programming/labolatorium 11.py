#Mateusz Błażejczyk
#zad 1
import math

a = float(input("Podaj wysokosc: "))
b = float(input("Podaj promień: "))

v = math.pi * pow(b, 2) * a
s = 2 * math.pi * pow(b, 2) + 2 * math.pi * b * a

print("powierzchnia wynosi: " + str(s) + " a objętość: " + str(v))



#zad 2
a = int(input("Podaj liczbe: "))

sum = 0
for i in range(a):
    if i == 0:
        continue
    if a % i == 0:
        sum += i

if a > sum:
    print("Liczba nie jest obfita")
else:
    print("Liczba jest obfita")


#zad 3
v = int(input("Podaj prędkośc wiatru: "))
t = int(input("Podaj temperature: "))

To = 13.12 + 0.6215 * t - 11.37 * pow(v, 0.16) + 0.3965 * t * pow(v, 0.16)

print("Temp odczuwalna to: " + str(To))


#zad 4
import math
from numpy import sin, cos, arccos, pi, round

psg = float(input("Podaj początkową szerokość geograficzną: "))
pdg = float(input("Podaj początkową długość geograficzną: "))
ksg = float(input("Podaj końcową szerokość geograficzną: "))
kdg = float(input("Podaj końcową długość geograficzną:  "))

theta = pdg - kdg

distance = 60 * 1.1515 * math.degrees(
    arccos(
        (sin(math.radians(psg)) * sin(math.radians(ksg))) +
        (cos(math.radians(psg)) * cos(math.radians(ksg)) * cos(math.radians(theta)))
    )
)

print(round(distance * 1.609344, 2))



#zad 5
a = complex(int(input("Real liczby a: ")), int(input("Imag liczby a: ")))
b = complex(int(input("Real liczby b: ")), int(input("Imag liczby b: ")))
print("Wyniki:")
dodawanie = complex(a.real + b.real, a.imag + b.imag)
print("Dodawanie: " + str(dodawanie))
odejmowanie = complex(a.real - b.real, a.imag - b.imag)
print("Odejmowanie: " + str(odejmowanie))
mnozenie = complex(a.real * b.real, a.imag * b.imag)
print("Mnożenie: " + str(mnozenie))
dzielenie = complex(a.real / b.real, a.imag / b.imag)
print("Dzielenie: " + str(dzielenie))


#zad 6
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = int(input("Podaj trzecia liczbe: "))
d = int(input("Podaj czwartą liczbe: "))
e = int(input("Podaj piąta liczbe: "))

srednia = (a + b + c + d + e)/5
licznik = pow(a - srednia, 2) + pow(b - srednia, 2) + pow(c - srednia, 2) + pow(d - srednia, 2) + pow(e - srednia, 2)
odch = pow(licznik/ 5, -1)
print(odch)