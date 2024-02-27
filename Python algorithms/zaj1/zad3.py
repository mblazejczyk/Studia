import random

lista = list(range(-2500, 2500))
random.shuffle(lista)
print(lista)

def check(l):
    leng = len(l)
    for i in range(leng - 1):
        if l[i] > l[i + 1]:
            return False
    return True

iloscSkokow = 0
while not check(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            tmp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = tmp
            iloscSkokow += 1

print(lista)
print("Zajelo to: " + str(iloscSkokow))