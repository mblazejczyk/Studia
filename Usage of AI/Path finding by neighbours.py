import math

punkty = {"A": [1, 1], "B": [5,8], "C": [7, 12], "D": [2, 9], "E": [7, 2], "F": [1, 12], "G": [4, 2]}
startowy = "G"
kordynaty_strt = punkty[startowy]
trasa = [startowy]
suma_odleglosci = []

def odleglosc(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))

def szukanie_trasy(strt):
    if len(punkty) == 1:
        trasa.append(startowy)
        suma_odleglosci.append(odleglosc(punkty[strt], kordynaty_strt))
        return 0
    odleglosci = {}
    for klucz, wartosc in punkty.items():
        if klucz == strt:
            continue
        odleglosci[klucz] = odleglosc(punkty[strt], punkty[klucz])
        print(str(strt) + " -> " + str(klucz) + " = " + str(odleglosci[klucz]))
    print("-----------------")
    trasa.append(str(min(odleglosci, key=odleglosci.get)))
    suma_odleglosci.append(float(min(odleglosci.values())))
    punkty.pop(strt)
    if len(punkty) > 0:
        szukanie_trasy(min(odleglosci, key=odleglosci.get))

szukanie_trasy(startowy)
print(trasa)
print(suma_odleglosci)
print(sum(suma_odleglosci))
