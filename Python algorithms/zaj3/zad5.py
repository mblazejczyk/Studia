binar = 111
bi = []
for i in range(len(str(binar))):
    bi.append(str(binar)[i])

dziesietny = 0

for i in range(len(bi)):
    if bi[i] == "1":
        dziesietny = dziesietny + pow(2, i)

print(dziesietny)