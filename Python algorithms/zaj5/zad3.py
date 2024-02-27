text = "6!ABC128"

def binarnie(p):
    liczba = p
    binar = []
    def dodaj(miejsce):
        while True:
            if len(binar) > miejsce:
                if binar[miejsce] == 0:
                    binar[miejsce] = 1
                    break
                else:
                    binar[miejsce] = 0
                    miejsce += 1
            else:
                binar.append(1)
                break

    while liczba != 0:
        dodaj(0)
        liczba -= 1

    tmp = binar[::-1]
    output = ""
    for i in range(len(tmp)):
        output += str(tmp[i])
    return output


def szyfrowanie(s):
    output = ""
    skip = 0
    for i in range(len(s)):
        if skip > 0:
            skip -= 1
            continue
        if s[i].isnumeric():
            tempNum = s[i]
            check = 1
            while True:
                if len(s) > i + check:
                    if s[i + check].isnumeric():
                        tempNum += s[i + check]
                        check += 1
                        skip += 1
                    else:
                        break
                else:
                    break
            output += str(binarnie(int(tempNum))) + " "
        else:
            tempNum = ord(s[i])
            output += str(binarnie(int(tempNum))) + " "
    return output


print(szyfrowanie(text))