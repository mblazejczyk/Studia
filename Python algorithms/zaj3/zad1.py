f = open("anagramy.txt", "r")
tekst = f.read()

odpowiedz = []
szukana = "AAB"

for i in range(len(tekst)):
    if i+2 <= len(tekst):
        if tekst[i] == szukana[0] and tekst[i+1] == szukana[1] and tekst[i+2] == szukana[2]:
            odpowiedz.append(i)

print(odpowiedz)