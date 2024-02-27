p1 = open("plik1.txt", "r").read()
p2 = open("plik2.txt", "r").read()

ind1 = []
ind2 = []
wsp = []
for i in range(len(p1.split(';'))):
    for j in range(len(p2.split(';'))):
        if p1.split(';')[i] == p2.split(';')[j]:
            wsp.append(p2.split(';')[j])
            break

for i in range(len(p1.split(';'))):
    f = False
    for j in range(len(wsp)):
        if p1.split(';')[i] == wsp[j]:
            f = True
            break
    if not f:
        ind1.append(p1.split(';')[i])

for i in range(len(p2.split(';'))):
    f = False
    for j in range(len(wsp)):
        if p2.split(';')[i] == wsp[j]:
            f = True
            break
    if not f:
        ind2.append(p2.split(';')[i])
print(ind1)
print(ind2)
print(wsp)