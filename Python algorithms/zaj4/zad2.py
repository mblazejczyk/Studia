alphabet = "abcdefghijklmnopqrstuvwxyz"
jawny = str(input("Podaj tekst do zaszyfrowania: "))
szyfr = int(input("Podaj liczbe (od 1 do 25) szyfrowania: "))


def szyfrowanie(text, liczba):
    newAlphabet = ""
    for i in range(len(alphabet)):
        if len(alphabet) <= i + liczba:
            for j in range(0, len(alphabet) - i):
                newAlphabet += alphabet[j]
            break
        else:
            newAlphabet += alphabet[i + liczba]

    output = ""
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                output += newAlphabet[j]
                break
    return output

def deszyfrowanie(text, liczba):
    newAlphabet = ""
    for i in range(len(alphabet)):
        if len(alphabet) <= i + liczba:
            for j in range(0, len(alphabet) - i):
                newAlphabet += alphabet[j]
            break
        else:
            newAlphabet += alphabet[i + liczba]

    output = ""
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == newAlphabet[j]:
                output += alphabet[j]
                break
    return output

print(szyfrowanie(jawny, szyfr))
print(deszyfrowanie(szyfrowanie(jawny, szyfr), szyfr))