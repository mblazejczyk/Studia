text = str(input("Podaj tekst do zaszyfrowania: "))

def szyfrowanie(s):
    output = ""
    for i in range(len(s) - 1, -1, -1):
        output += s[i]
    return output

print(szyfrowanie(text))
print(szyfrowanie(szyfrowanie(text)))