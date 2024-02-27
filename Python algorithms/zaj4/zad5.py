alphabet = "abcdefghijklmnopqrstuvwxyz"
jawny = str(input("Podaj tekst do zaszyfrowania: "))
szyfr = int(input("Podaj liczbe (od 1 do 25) szyfrowania: "))


def czyMala(litera):
    return 'a' <= litera <= 'z'


def czyDuza(litera):
    return 'A' <= litera <= 'Z'


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
        if czyMala(text[i]):
            for j in range(len(alphabet)):
                if text[i] == alphabet[j]:
                    output += newAlphabet[j]
                    break
        elif czyDuza(text[i]):
            for j in range(len(alphabet)):
                if text[i].lower() == alphabet[j]:
                    output += newAlphabet[j].upper()
                    break
        else:
            output += text[i]

    return output


zaszyfrowany_tekst = szyfrowanie(jawny, szyfr)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
