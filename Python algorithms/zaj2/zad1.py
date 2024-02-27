import random

szukana = random.randint(0, 1000)
strzal = 0
min = 0
max = 1000
while strzal != szukana:
    strzal = random.randint(min, max)
    if strzal > szukana:
        max = szukana
    elif strzal < szukana:
        min = szukana
    else:
        break
print(strzal)