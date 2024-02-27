#Mateusz Błażejczyk
#zad 1
lista2 = list(range(0, 10, 1))
print("lista2 = ", lista2, ".", sep = "")

lista4 = [1, 2, 3]
for i in range(len(lista4)):
 lista4[i] = lista4[i] * 5
print(lista4)

lista5=[]
for x in range(0, 100, 10):
 lista5.append(x)
for i in lista5:
 print(i, end=' ')

def dlugie_slowa(n, lista6):
 lista_dlugie_slowa = []
 tekst = lista6.split(" ")
 for x in tekst:
  if len(x) > n:
   lista_dlugie_slowa.append(x)
  return lista_dlugie_slowa
print(dlugie_slowa(7, "W Szczebrzeszynie chrząszcz brzmi w trzcinie, i Szczebrzeszyn z tego słynie."))

def pierwsze_znaki(lista7, znak):
 result = [i for i in lista7 if i.startswith(znak)]
 return result
lista7 = ["cdba", "abcd", "adbg", "bacd", "bdac", "cdae", "mwar", "sgrs",
"atre"]
print("\nLista poczatkowa:")
print(lista7)
znak = "a"
print("\nElementy zaczynajace sie na",znak)
print(pierwsze_znaki(lista7, znak))







#zad2
list = [1.1, 2.2, 3.3]
il = list[0] * list[1] * list[2]
print(format(il, '.3f'))


#zad 3
def funkcja(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x

    min = lista[0]
    for x in lista:
        if x < min:
            min = x
    print("Najwieksza liczba to: " + str(max) + " a najmniejsza: " + str(min))


l1 = [1, 3, 2]
funkcja(l1)



#zad 4
def funkcja(lista):
    l2 = []
    for i in range(len(lista)):
        x = 0
        for j in range(len(l2)):
            if lista[i] == l2[j]:
                x = 1
                break
        if x == 0:
            l2.append(lista[i])
    print(l2)


l1 = [1, 3, 2, 3, 4, 5, 1]
funkcja(l1)



#zad5
def funkcja(lista):
    l2 = ""
    for i in range(len(lista)):
        l2 += lista[i]
    print(l2)


l1 = ['c', 'z', 'e', 'ś', 'ć']
funkcja(l1)



#zad6
def funkcja(lista1, lista2):
    l3 = []
    for i in range(len(lista1)):
        x = 0
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                l3.append(lista1[i])
    print(l3)


l1 = [1, 3, 2, 9, 4, 5, 1]
l2 = [11, 12, 13, 3, 14, 15, 5]
funkcja(l1, l2)




#zad7
def funkcja(lista1, n):
    l2 = []
    i = 0
    for j in range(int(len(lista1)/n)):
        l2.append([])
        i = j
        while i < len(lista1):
            l2[j].append(lista1[i])
            i += 3
    print(l2)



l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
funkcja(l1, 3)




#zad8
def funkcja(lista1, lista2):
    l3 = lista1
    for j in range(len(lista2)):
        l3.append(lista2[j])
    print(l3)



l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9]
funkcja(l1, l2)




#zad9
def funkcja(lista1, st):
    l3 = []
    for j in range(len(lista1)):
        l3.append(st + str(lista1[j]))
    print(l3)



l1 = [1, 2, 3, 4]
s = "budynek"
funkcja(l1, s)




#zad10
def funkcja(lista1):
    l2 = []
    ilezer = 0
    for j in range(len(lista1)):
        if lista1[j] == 0:
            ilezer += 1
        else:
            l2.append(lista1[j])

    for i in range(ilezer):
        l2.append(0)
    print(l2)



l1 = [1, 2, 0 ,3, 0 ,4, 5, 6, 0]
funkcja(l1)




#zad11
def finkcja(n):
    if n < 2:
        print("Brak liczb pierwszych w podanym zakresie")
    else:
        skr = [False] * (n + 1)
        i = 2
        while i * i <= n:
            if not skr[i]:
                j = i * i
                while j <= n:
                    skr[j] = True
                    j += i
            i += 1
        for i in range(2, n+1):
            if not skr[i]:
                print(i, end = " ")

finkcja(100)