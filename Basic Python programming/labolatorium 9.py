#Zad 2
krotka = (1, 2, 3, 4, 5)
lista = list(krotka)
element = 3
lista.remove(element)
krotka = tuple(lista)
print(krotka)


#zad 3
krotki = [(1, 2), (3, 4), (1, 3), (1, 2)]
wartosc = 1
def indeksy(kolekcja, wartosc):
    indeksy = []
    for i, element in enumerate(kolekcja):
        if wartosc in element:
            indeksy.append(i)
    return indeksy

print(indeksy(krotki, wartosc))


#zad 4
krotka = (1, 2, 3, 4, 5)
odwrocona = []
i = len(krotka) - 1
while i != -1:
    odwrocona.append(krotka[i])
    i -= 1

odwrocona_krotka = tuple(odwrocona)
print(odwrocona_krotka)


#zad 5
list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

i = 0
while i != len(list2):
    j = 0
    list_temp = []
    while j != len(list2[i]) - 1:
        list_temp.append(list2[i][j])
        j += 1
    list_temp.append(0)
    list2[i] = list_temp
    i += 1

print(list2)


#zad 6
list2 = [(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]
list3 = []
i = 0
while i != len(list2):
    j = 0
    list_temp = []
    if len(list2[i]) > 0:
        while j != len(list2[i]):
            list_temp.append(list2[i][j])
            j += 1
        list3.append(tuple(list_temp))
    i += 1

print(list3)



#zad 7
def sortowanie_babelkowe(x):
    lista = list(x)
    n = len(lista)
    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if lista[l] > lista[l + 1]:
                lista[l], lista[l + 1] = lista[l + 1], lista[l]
                zamien = True
        n -= 1
        if zamien == False: break
    return tuple(lista)

krotka = (5, 6, -1, 0)
print(sortowanie_babelkowe(krotka))



#zad 8
s = "Czesc"

def tekstNaKropke(t):
  temp = []
  i = 0
  while i != len(t):
      temp.append(t[i])
      i += 1
  return tuple(temp)


print(tekstNaKropke(s))



#zad 9
krotka = ((1, 2, 3, 4), (10, 15, 25, 35), (70, 80, 90, 100), (-20, -15, -10, -5))

def Srednia(k):
  temp = []
  i = 0
  while i != len(k):
      j = 0
      srednia = 0
      while j != len(k[i]):
          srednia += k[j][i]
          j += 1
      srednia = srednia / len(k[i])
      temp.append(srednia)
      i += 1
  return temp


print(Srednia(krotka))



#zad 10
krotka = (('pon', 'wto', 'srd'), ('czw', 'ptk', 'sob'), ('ndz', 'pon', 'wto'))

def Srednia(k, wartosc):
  i = 0
  czyWyst = 0
  while i != len(k):
      j = 0
      while j != len(k[i]):
          if k[i][j] == wartosc:
              czyWyst = 1
          j += 1
      i += 1
  if czyWyst == 1:
      return True
  else:
      return False


print(Srednia(krotka, str(input("Podaj wartosc do sprawdzenia: "))))