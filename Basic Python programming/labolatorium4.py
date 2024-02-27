#Mateusz Błażejczyk

#Zadanie 2
def najwieksza(in1, in2, in3):
    if in1 > in2:
        if in1 > in3:
            print("Największą liczbą jest: " + str(in1))
        else:
            print("Największą liczbą jest: " + str(in3))
    else:
        if in2 > in3:
            print("Największą liczbą jest: " + str(in2))
        else:
            print("Największą liczbą jest: " + str(in3))


i1 = int(input("Podaj pierwsza liczbe: "))
i2 = int(input("Podaj druga liczbe: "))
i3 = int(input("Podaj trzecia liczbe: "))
najwieksza(i1, i2, i3)


#zadanie 3
def odwrotnosc(st):
    i = len(st) - 1
    newSt = ""
    while i >= 0:
        newSt += st[i]
        i -= 1
    print(newSt)

s = input("Podaj pierwsza liczbe: ")
odwrotnosc(s)




#zadanie 4
def isBetween(inte):
    if inte >= 0:
        if inte <= 100:
            print("Liczba jest w przedziale od 0 do 100")
        else:
            print("Liczba NIE jest w przedziale od 0 do 100")
    else:
        print("Liczba NIE jest w przedziale od 0 do 100")

i = input("Podaj liczbe: ")
isBetween(int(i))




#zadanie 5
def silnia(inte):
    i = inte
    sil = 1
    while i > 0:
        sil *= i
        i -= 1
    print(sil)

s = input("Podaj liczbe: ")
silnia(int(s))




#zadanie 6
def iloscWielk(st):
    i = len(st) - 1
    iloscDuzych = 0
    iloscMal = 0
    while i >= 0:
        if st[i].islower():
            iloscMal += 1
        else:
            iloscDuzych += 1
        i -= 1
    print("Malych liter jest: " + str(iloscMal) + " a duzych: " + str(iloscDuzych))

s = input("Podaj tekst: ")
iloscWielk(str(s))




#zadanie 7
def czyDoskonala(st):
    suma = 0
    i = st
    akDziel = 1
    while i > 1:
        if st % akDziel == 0:
            suma += akDziel
        akDziel += 1
        i -= 1
    if suma == st:
        print("Liczba jest doskonała")
    else:
        print("Liczba NIE jest doskonała")

s = input("Podaj liczbe: ")
czyDoskonala(int(s))




#zadanie 8
def czyPalindromem(st):
    sprawpocz = 0
    sprawOs = len(st) - 1
    while sprawpocz != sprawOs:
        if st[sprawpocz] != st[sprawOs]:
            print("Nie jest to palindrom")
            return
        sprawpocz += 1
        sprawOs -= 1
    print("Jest to palindrom")


s = input("Podaj słowo: ")
czyPalindromem(str(s))





#zadanie 9
import random

def randomPierw():
    losowaLicz = random.randint(0, 1000)
    aktualnyWyn = losowaLicz
    i = 100
    while i != 0:
        aktualnyWyn = (1/aktualnyWyn) * (aktualnyWyn + (losowaLicz/2))
        print(aktualnyWyn)
        i -= 1
    print(round(aktualnyWyn, 0))

randomPierw()