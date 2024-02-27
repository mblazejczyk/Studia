#Mateusz Blazejczyk
#zad 2
i = 0
while i < 30:
    if i % 3 == 0:
        print(i)
    i += 1



#zad 3
for i in range(31):
    if i % 2 != 0:
        continue
    print(i)



#zad 4
def alfabet(x):
    alfabet1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alfabet1)):
        if alfabet1[i] != x:
            print(alfabet1[i])
        else:
            break
    print(x)

alfabet(input("Podaj litere: "))



#zad 5
def suma(x):
    sumaLiczb = 0
    for i in range(x + 1):
        sumaLiczb += i
    print(sumaLiczb)

suma(int(input("Podaj litere: ")))



#zad 6
def parzyste(x):
    sumaLiczb = 0
    for i in range(x + 1):
        if(i % 2 == 0):
            sumaLiczb += i
    print(sumaLiczb)

parzyste(int(input("Podaj litere: ")))



#zad 7
def program():
    i = 100
    while i != -100:
        i -= 1
        if(i % 2 != 0 or i % 3 == 0 or i % 8 == 0):
            continue
        print(i)

program()



#zad 8
def ocena(x1, x2, x3, x4, x5):
    tablica = [x1, x2, x3, x4, x5]
    tablica.sort()
    if(x1 > 20 or x1 < 0 or x2 > 20 or x2 < 0 or x3 > 20 or x3 < 0 or
        x4 > 20 or x4 < 0 or x5 > 20 or x5 < 0):
        print("Podano ocene spoza zakresu")
        return
    suma = tablica[1] + tablica[2] + tablica[3]
    print(suma)

ocena(int(input("Podaj pierwszą ocene: ")), int(input("Podaj druga ocene: ")),
      int(input("Podaj trzecia ocene: ")), int(input("Podaj czwarta ocene: ")),
        int(input("Podaj piata ocene: ")))



#zad 9
def ocena(n):
    tablica = []
    for i in range(n):
        tablica.append([])
        for j in range(n):
            if i + 1 < j + 1:
                tablica[i].append(i + 1)
            else:
                tablica[i].append(j + 1)

    for i in range(n):
        print(tablica[i])


ocena(int(input("Podaj pierwszą ocene: ")))



#zad 10
def ciagAryt(n, a1, d):
    if n == 1:
        return a1
    else:
        return ciagAryt(n-1, a1, d) + d


print(ciagAryt(int(input("Podaj numer wyrazu: ")), int(input("Podaj pierwszy wyraz ciagu: ")),
         int(input("Podaj różnice ciagu: "))))




#zad 11
def fun(n):
    dane = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P']
    output =[]
    for i in range(n):
        output.append([])
    for i in range(n):
        j = i
        while j < len(dane):
            output[i].append(dane[j])
            j += n
    print(output)

fun(int(input("Podaj n: ")))




#zad 12
def fun():
    d1 = [100, 90, 80, 70, 60, 50]
    d2 = [49, 39, 29, 19]
    output = []
    for i in range(len(d1) + len(d2)):
        if len(d1) > len(output):
            output.append(d1[i])
        else:
            output.append(d2[i - len(d1)])
    print(output)

fun()




#zad 13
def fun(n, a):
    d1 = n
    output = []
    for i in range(len(d1)):
        output.append(a + str(d1[i]))
    print(output)

fun(['A', 'B', 'C', 'D'], "Exit ")




#zad 14
def fun(n):
    d1 = n
    output = ""
    for i in range(len(d1)):
        output += d1[i]
    print(output)

fun(['H', 'e', 'l', 'l', 'o'])




#zad 15
def fun(n, a):
    d1 = n
    d2 = a
    output = []
    for i in range(len(d1)):
        for j in range(len(d2)):
            if d1[i] == d2[j]:
                output.append(d2[j])
    print(output)

fun(['H', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd'])




#zad 16
def fun(n):
    d1 = n
    output = []
    ilosc = 0
    for i in range(len(d1)):
        if d1[i] == 1:
            ilosc += 1
        else:
            output.append(d1[i])
    for i in range(ilosc):
        output.append(1)
    print(output)

fun([3, 5, 1, 4, 1, 2, 11, 7, 1, 5, 9, 1])




#zad 17
def fun(n):
    output = 1.0
    for i in n.values():
        output *= i
    return output


print(fun({ 'f1': 4.8, 'f2': 2.4, 'f3': 1.2, 'f4': 0.6}))




#zad 18
def fun(n):
    output = {}
    for i in range(n + 1):
        if i == 0: continue
        nazwa = str(i)
        wynik = i ** 4
        output.update({nazwa: wynik})
    print(output)


fun(int(input("podaj n: ")))




#zad 19
def fun(n):
    s1 = n
    output = []
    for i in range(len(s1) + 1):
        if i == 0: continue
        check = False
        for j in range(len(output)):
            if s1[i] == output[j]:
                check = True
        if check == False:
            output.append(s1[i])
    otpSlownik = {}
    for j in range(len(output)):
        otpSlownik.update({str(j): output[j]})
    return otpSlownik.values()

input = {1: 'A201', 2: 'B218', 3:'H018', 4:'B218', 5:'H018', 6: 'G123', 7: 'A007', 8: 'G230'}
print(fun(input))