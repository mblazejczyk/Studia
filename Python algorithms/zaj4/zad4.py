text = str(input("Podaj tekst do zaszyfrowania: "))

def szyfrowanie(s):
    output = ""
    for i in range(len(s)):
        output += chr(255 - ord(s[i]))
    return output

print(szyfrowanie(text))
