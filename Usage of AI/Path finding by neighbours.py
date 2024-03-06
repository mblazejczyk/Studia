import math

punkty = {}
while True:
    print(punkty)
    print("Podaj kolejno nazwe punktu a później koordynaty. Jeśli podałeś już punkty, wpisz stop")
    tmp1 = str(input("Podaj nazwe punktu: "))
    if tmp1 == "stop":
        break
    tmp2 = int(input("Podaj położenie X: "))
    tmp3 = int(input("Podaj położenie Y: "))
    tmp4 = [tmp2, tmp3]
    punkty[tmp1] = tmp4
    print("------------Dodano-----------")
startowy = str(input("Podaj punkt startowy: "))
print("--------------------------")
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
print("Kolejnośc odwiedzanych punktów:")
print(trasa)
print("\nOdległości pomiędzy punktami:")
print(suma_odleglosci)
print("\nSuma odległości:")
print(sum(suma_odleglosci))
