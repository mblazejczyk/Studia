s = "ZXYBCA"

#Przygotowanie słownika
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
slownik = {}
for i in range(len(alf)):
    slownik[alf[i]] = 0

#zliczanie
for i in range(len(s)):
    slownik[s[i]] += 1

#wstawienie
final = ""
for i in range(len(alf)):
    for j in range(slownik[alf[i]]):
        final += alf[i]

print(final)