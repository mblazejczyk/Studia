text = "6A3B3A2B1A"

def deszyfrowanie(s):
    output = ""
    for i in range(len(text)):
        if text[i].isnumeric():
            for j in range(int(s[i])):
                output += s[i + 1]
    return output

print(deszyfrowanie(text))