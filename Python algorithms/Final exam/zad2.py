l1 = "AABBCCDDA"
l2 = "AACCDADA"

def pobierzSrodek(st, pocz, kon):
    final = ""
    for i in range(len(st)):
        if i >= pocz and i <= kon:
            final += st[i]
    return final

lastFound = ""
for szukanaDLugosc in range(1, len(l1)):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if len(l1) < i + szukanaDLugosc or len(l2) < j + szukanaDLugosc:
                break
            f1 = pobierzSrodek(l1, i, i + szukanaDLugosc)
            f2 = pobierzSrodek(l2, j, j + szukanaDLugosc)
            if f1 == f2:
                if len(f1) > len(lastFound):
                    lastFound = pobierzSrodek(l1, i, i + szukanaDLugosc)

print(lastFound)