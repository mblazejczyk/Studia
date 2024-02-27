inp = "!AB#"

otp = []
for i in range(len(inp)):
    otp.append(ord(inp[i]))
print(otp)

b = []
for i in range(len(otp)):
    b.append("")
    for j in reversed(range(8)):
        if otp[i] - pow(2, j) >= 0:
            b[i] += "1"
            otp[i] -= pow(2, j)
        else:
            b[i] += "0"
print(b)

o = ""
failcheck = 0
for i in range(len(b)):
    o += b[i]
    if b[i] == "00000000":
        failcheck += 8
    if failcheck == 256:
        o += "11111111"
print(o)

o2 = ""
last = int(o[0])
x = 0
for i in range(len(o)):
    if int(o[i]) == last:
        x += 1
    else:
        o2 += str(x)
        x = 1
        last = int(o[i])

print(o2)
final = ""
for i in range(len(o2)):
    final += chr(int(o2[i]))
print(final)
