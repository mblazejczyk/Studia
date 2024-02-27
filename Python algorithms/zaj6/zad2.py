def zad1(s):
    inp = s

    otp = []
    for i in range(len(inp)):
        otp.append(ord(inp[i]))

    b = []
    for i in range(len(otp)):
        b.append("")
        for j in reversed(range(8)):
            if otp[i] - pow(2, j) >= 0:
                b[i] += "1"
                otp[i] -= pow(2, j)
            else:
                b[i] += "0"

    o = ""
    for i in range(len(b)):
        o += b[i]

    o2 = []
    last = int(o[0])
    x = 0
    for i in range(len(o)):
        if int(o[i]) == last:
            x += 1
        else:
            o2.append(x)
            x = 1
            last = int(o[i])

    return o2

z1 = zad1("!AB#")
N = 2

z1 = [2, 1, 3, 4, 2, 5]
tempar = []
for i in range(len(z1)):
    if z1[i] >= pow(2, N):
        while True:
            tmp = z1[i]
            s = ""
            s2 = ""
            for j in range(N):
                s += "1"
                s2 += "0"
            tempar.append(s)
            tempar.append(s2)

            reduce = 0
            for i in range(N):
                reduce += pow(2, i)
            tmp -= reduce


            if tmp < pow(2, N):
                b = ""
                for j in reversed(range(N)):
                    if tmp - pow(2, j) >= 0:
                        b += "1"
                        tmp -= pow(2, j)
                    else:
                        b += "0"
                tempar.append(b)
                break
    else:
        tmp = z1[i]
        b = ""
        for j in reversed(range(N)):
            if tmp - pow(2, j) >= 0:
                b += "1"
                tmp -= pow(2, j)
            else:
                b += "0"
        tempar.append(b)

print(z1)
print(tempar)
f = open("output.txt", "a")

b = ""
tmp = N
for j in reversed(range(8)):
    if tmp - pow(2, j) >= 0:
        b += "1"
        tmp -= pow(2, j)
    else:
        b += "0"
f.write(str(int(b).to_bytes(8, byteorder='big')))

final = ""
for i in range(len(tempar)):
    final += tempar[i]

while len(final) % 8 != 0:
    final += "0"

print(final)
for i in range(0, len(final), 8):
    segment = final[i:i+8]
    f.write(str(int(segment).to_bytes(8, byteorder='big')))

f.close()