#zad 2
def sumuj_liste(lista):
 if len(lista) == 1:
  return lista[0]
 else:
  return lista[0] + sumuj_liste(lista[1:])

print(sumuj_liste([1, 2, 3, 4, 5]))



#zad 3
def sumuj(liczba):
 if len(liczba) == 1:
  return int(liczba[0])
 else:
  return int(liczba[0]) + int(sumuj(liczba[1:]))

a = input("Podaj liczbe: ")
print(sumuj(a))



#zad4
def fino(pop2, pop):
 sum = pop2 + pop
 print(sum)
 if sum > 500:
  return 1
 fino(pop, sum)

fino(0, 1)



#zad 5
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
print(a)




#zad 6
def wspol_dziel(licz1, licz2):
    if licz2 > 0:
        return wspol_dziel(licz2, licz1 % licz2)
    else:
        return licz1

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(wspol_dziel(a, b))




#zad 7
a1 = int(input("podaj a1: "))
a2 = int(input("podaj a2: "))
def nty(n):
    if n == 1:
        return a1
    if n == 2:
        return a2

    return nty(1) + (n - 1) * (nty(2) - nty(1))

a = int(input("Podaj n: "))
print(nty(a))




#zad 8
a1 = int(input("podaj a1: "))
a2 = int(input("podaj a2: "))
def nty(n):
    if n == 1:
        return a1
    if n == 2:
        return a2

    return nty(1) * pow(nty(1)/nty(2), n-1)

a = int(input("Podaj n: "))
print(nty(a))