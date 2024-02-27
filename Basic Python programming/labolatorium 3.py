#Mateusz Błażejczyk
#zad 1
for i in range(2):
    print("for: " + str(i))
    while True:
        print("while")
        break




#zad 2
for i in range(10):
    print(i + 1)

j = 1
while j < 11:
    print(j)
    j += 1




#zad 3
x = int(input("Podaj liczbe: "))
y = 1

for i in range(x + 1):
    if i == 0:
        continue
    y *= i

print(y)



#zad 4
for i in range(21):
    if (i % 2) == 0:
        print(i)




#zad 5
i = 0
while i < 31:
    if (i % 3) == 0:
        print(i)
    i += 1




#zad 6
for i in range(31):
    if (i % 3) != 0:
        continue
    print(i)




#zad 7
x = input("Podaj litere: ")
alf = "abcdefghijklmnopqrstuvwxyz"
i = 0

while alf[i] != x:
    print(alf[i])
    i += 1
print(x)




#zad 8
x = int(input("Podaj liczbe: "))
y = 0
sum = 0
while y != x + 1:
    sum += y
    y += 1
print(sum)



#zad 9
x = int(input("Podaj liczbe: "))
y = 0
sum = 0
while y != x + 1:
    if (y % 2) == 0:
        sum += y
    y += 1
print(sum)




#zad 10
i = 100
while i >= 0:
    if (i % 3) == 0:
        if (i % 2) != 0:
            print(i)
    i -= 1

x = 100
for y in range(100):
    if (x % 3) == 0:
        if (x % 2) != 0:
            print(x)
    x -= 1




#zad 11
x = 100
for y in range(200):
    if (x % 2) == 0:
        if (x % 3) != 0:
            if(x % 8) != 0:
                print(x)
    x -= 1




#zad 12
for x in range(8):
    for y in range(8):
        if (x % 2) == 0:
            if (y % 2) == 0:
                print(1, end=' ')
            else:
                print(0, end=' ')
        else:
            if (y % 2) == 0:
                print(0, end=' ')
            else:
                print(1, end=' ')
    print("")




#zad 13
for y in range(6):
    for x in range(11):
        z = x * y
        print(str(x) + " * " + str(y) + " = " + str(z))