text = "AAAAAABBBAAABBA"

def szyfrowanie(s):
    lastChar = s[0]
    x = 0
    output = ""
    for i in range(len(text)):
        if lastChar == s[i]:
            x += 1
        else:
            output += str(x) + lastChar
            x = 1
            lastChar = s[i]
    output += str(x) + lastChar
    return output

print(szyfrowanie(text))