import  random

def zaokraglenie(n):
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1

lista = list(range(1, 1001))

szukana = int(random.randint(1, lista[len(lista) - 1]))
lewo = 0
prawo = lista[len(lista) - 1]
srodek = 1

iloscSkokow = 0
while lewo <= prawo:
    iloscSkokow += 1
    srodek = zaokraglenie((lewo + prawo) / 2)
    if lista[srodek] < szukana:
        lewo = srodek + 1
    elif prawo > szukana:
        prawo = srodek - 1
    else:
        break



print(lista[srodek])
print("Znaleziono w: " + str(iloscSkokow))