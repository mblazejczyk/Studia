liczba = 17
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

print(binar[::-1])
