#Mateusz Błażejczyk

#zad2
t1 = [1, 2, 3, 4]
t2 = [5, 6, 7, 8]
#t1.extend(t2)
i = 0
while i != len(t2):
    t1.append(t2[i])
    i += 1
print(t1)




#zad 3
t1 = [1, 2, 3, 4, 2, 6, 7, 4, 8, 2, 2, 9]
i = t1.count(2)
j = 0
while j != len(t1):
    if t1[j] == 2:
        break
    j += 1
print(str(i) + " razy wystąpiła cyfra 2 w " + str(j) + " miejscu po raz pierwszy")




#zad4
tab1 = []
for x in range(20):
    tab1.append(x + 1)
tab1.reverse()

tab2 = []
i = 0
while i != len(tab1) - 1:
    i += 1
    if (tab1[i] % 3) == 0:
        tab2.append(i)
    elif (tab1[i] % 7) == 0:
        tab2.append(i)
    else:
        continue

i = 0
for x in tab2:
    tab1.pop(x - i)
    i += 1

print(tab1)




#zad5
tab1 = []
i = 0
while i != 15:
    i += 1
    tab1.append(int(input("Podaj kolejna liczbe: ")))

j = 0
sum = 0
while j != len(tab1) - 1:
    sum += float(tab1[j])
    j += 1
sum = sum / j
print(sum)





#zad6
tab1 = []
i = 0
while i != 4:
    i += 1
    tab1.append(int(input("Podaj kolejna liczbe: ")))

max = 0
min = 0
if tab1[0] > tab1[1] and tab1[0] > tab1[2] and tab1[0] > tab1[3]:
    max = tab1[0]
elif tab1[1] > tab1[0] and tab1[1] > tab1[2] and tab1[1] > tab1[3]:
    max = tab1[1]
elif tab1[2] > tab1[1] and tab1[2] > tab1[0] and tab1[2] > tab1[3]:
    max = tab1[2]
else:
    max = tab1[3]

if tab1[0] < tab1[1] and tab1[0] < tab1[2] and tab1[0] < tab1[3]:
    min = tab1[0]
elif tab1[1] < tab1[0] and tab1[1] < tab1[2] and tab1[1] < tab1[3]:
    min = tab1[1]
elif tab1[2] < tab1[1] and tab1[2] < tab1[0] and tab1[2] < tab1[3]:
    min = tab1[2]
else:
    min = tab1[3]
print("Maksymalna to: " + str(max) + " a minimalna to: " + str(min))





#zad7
tab1 = []
i = 0
while i != 5:
    inp = int(input("Podaj kolejna liczbe: "))
    if inp >= 0 and inp <= 20:
        i += 1
        tab1.append(inp)
    else:
        print("Podano niepoprawny wynik")

tab1.sort()
max = tab1[-1]
min = tab1[0]
sum = tab1[0] + tab1[1] + tab1[2] + tab1[3] + tab1[4]
sum -= max
sum -= min
print("Ostateczny wynik to: " + str(sum))





#zad8
tab = []
n = 5
i = 0
while i != n:
    tab.append([i + 1])
    j = tab[-1][-1]
    x = j
    y = 1
    while y != x:
        tab[j - 1][0] = 1
        tab[j - 1].append(y + 1)
        y += 1
    while x != n:
        tab[j - 1].append(j)
        x += 1
    print(tab[i])
    i += 1





#zad9
tab = []
x = 3
y = 4

i = 0
while i != x:
    tab.append([i])
    j = 0
    while j != y:
        tab[i].append(j)
        j += 1
    i += 1

i = 0
while i != x:
    j = 0
    while j != y + 1:
        tab[i][j] = (i + 1) * (j + 1)
        j += 1
    print(tab[i])
    i += 1