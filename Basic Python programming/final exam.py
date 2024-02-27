#Mateusz Błażejczyk
#zad 1
d1 = [1,12,6,9,7,5,3,4,5,4,5,9,13,8,7,2,3]
ile = 5
while ile != 0:
    for i in range(len(d1)):
        if d1[i] % 2 == 0:
            d1.pop(i)
            ile -= 1
            break

print(d1)



#zad 2
n = int(input("Podaj liczbe: "))
x = n
d1 = []
for i in range(n + 1):
    d1.append([])
    while x != 0:
        if x < i:
            d1[i].append(i)
        else:
            d1[i].append(x)
        x -= 1
    x = n
d1.pop(0)

for i in range(len(d1)):
    print(d1[i])




#zad 3
d1 = []
n = int(input("Podal wielkość trójkąta: "))

for i in range(n):
    d1.append([])
    for j in range(i + 1):
        if j == 0 or j == i:
            d1[i].append(1)
        elif i == 1:
            d1[i].append(1)
        else:
            d1[i].append(d1[i - 1][j - 1] + d1[i - 1][j])

output = ""
for i in range(len(d1)):
    print(d1[i])
    for j in range(len(d1[i])):
        output += "|" +  str(d1[i][j]) + "|"
    output += '\n'

f = open('pascal.txt', 'w')
f.write(output)




#zad 4
d1 = [(2, 1, -3), (13, 0, 76), (4, 7), (-4, 3, -2, 1)]
output = []
for i in range(len(d1)):
    tamp = list(d1[i])
    ilocz = 1
    for j in range(len(tamp)):
        ilocz *= tamp[j]
    output.append(ilocz)
print(output)