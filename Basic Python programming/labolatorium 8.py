#Mateusz Błażejczyk
#zad 2
slownik = { 'd1':1.1, 'd2':2.2, 'd3':3.3}
iloczyn = 1
for klucz, wartosc in slownik.items():
 iloczyn *= wartosc

print("%.3f" % iloczyn)



#zad 3
slownik1 = { 'd1':1.1, 'd2':2.2, 'd3':3.3}
slownik2 = {'B': 1, 'Czerwony': 2, 'Zielony': 3, 'Niebieski': 4, 'Czarny':
5}
for klucz, wartosc in slownik2.items():
 slownik1.update(slownik2)

print(slownik1)



#zad 4
slownik1 = {}

for x in range(6):
 if x == 0: continue
 p = pow(x, 3)
 slownik1.update({x : p})


print(slownik1)



#zad 5
slownik1 = {'Bialy': 1, 'Czerwony': 2, 'Zielony': 3, 'Niebieski': 4, 'Czarny':
5}

slownik2 = {}
slownik2 = sorted(slownik1.items())

print(slownik2)



#zad 6
slownik1 = {'a': 'A201', 'b': 'B202', 'c':'B202', 'd':'H018',
            'e':'H018', 'f': 'A007', 'g': 'A230'}

slownik2 = []

for klucz, wartosc in slownik1.items():
    if len(slownik2) == 0:
        slownik2.append(wartosc)
        continue
    n = 0
    for x in range(len(slownik2)):
        if slownik2[x] == wartosc:
            n = 1

    if n == 0:
        slownik2.append(wartosc)


print(slownik2)



#zad 7
ciag = "abcdefg"
slownik1 = {}

for x in range(len(ciag)):
    slownik1.update({(x + 1) : ciag[x]})

print(slownik1)



#zad 8
slownik1 = {'a': 'A201', 'b': 'B202', 'c':'B202', 'd':'H018',
            'e':'H018', 'f': 'A007', 'g': 'A230', 'h' : 'B202'}

slownik3 = {}
print("Wzór outputu: {'wartosc' : 'ile wystepuje'}")
for klucz, wartosc in slownik1.items():
    n = 0
    for x, y in slownik1.items():
        if y == wartosc:
            n += 1

    slownik3.update({wartosc : n})


print(slownik3)