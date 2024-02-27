def wykrSys(liczba):
    alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lS = f"{liczba}"
    najwieksza = 0
    for i in range(len(lS)):
        for j in range(len(alf)):
            if lS[i] == alf[j] and j > najwieksza:
                najwieksza = j
                break

    liczbaStr = f"{liczba}"[::-1]
    nowa = 0
    for i in range(len(liczbaStr)):
        for j in range(len(alf)):
            if liczbaStr[i] == alf[j]:
                nowa += j * ((najwieksza + 1) ** i)
    return f"Najmniejszy system to: {najwieksza + 1} \na jego reprezentacja w dziesietnym to {nowa}"

print(wykrSys("F12F"))