#Mateusz Blazejczyk
#zad 2
import datetime
z = datetime.date.today() + datetime.timedelta(weeks = 1)
print(z)


#zad 3
import datetime
z = datetime.date.today()
print(z)

while str(z) != '2023-02-15':
    if z.strftime("%A") == 'Tuesday':
        print(z)
    z += datetime.timedelta(days=1)


#zad 4
import datetime
z = datetime.datetime(2023, 1, 6)
x = 0
while True:
    if z.strftime("%A") == 'Sunday':
        print(z)
        x += 1
        z = datetime.datetime(2023, 1, 6) + datetime.timedelta(days=(x*365))
    z += datetime.timedelta(days=1)
    if x == 3:
        break



#zad 5
import datetime
z = datetime.datetime(2023, 9, 1)

while z.strftime("%A") != 'Monday':
    z += datetime.timedelta(days=1)
print(z)


#zad 6
import datetime
z = datetime.date.today() + datetime.timedelta(days=100)

print(z)


#zad 7
import datetime
z = datetime.datetime(2023, 3, 1)
lista = []
while z != datetime.datetime(2023, 6, 10):
    if z.strftime("%A") == 'Saturday':
        lista.append(z.strftime("%x"))
    z += datetime.timedelta(days=1)
print(lista)


#zad 8
import datetime
z = datetime.datetime(2023, 1, 1)
lista = []
last = datetime.datetime(2023, 1, 1)
while z != datetime.datetime(2023, 12, 31):
    if z.strftime("%b") != last.strftime("%b"):
        lista.append(last.strftime("%x"))
    if z.strftime("%A") == 'Sunday':
        last = z

    z += datetime.timedelta(days=7)
print(lista)


#zad 9
import datetime
data1 = input("Podaj pierwszą date w formacie 2023-1-1: ")
godzina1 = input("Podaj pierwszą godzine w formacie 9:10:0 : ")
data11 = data1.split('-')
godzina11 = godzina1.split(':')
z = datetime.datetime(int(data11[0]), int(data11[1]), int(data11[2]), int(godzina11[0]), int(godzina11[1]), int(godzina11[2]))

data1 = input("Podaj drugą date w formacie 2023-1-1: ")
godzina1 = input("Podaj drugą godzine w formacie 9:10:0 : ")
data11 = data1.split('-')
godzina11 = godzina1.split(':')
y = datetime.datetime(int(data11[0]), int(data11[1]), int(data11[2]), int(godzina11[0]), int(godzina11[1]), int(godzina11[2]))

x = y - z
print(str(x.total_seconds()) + " sekund różnicy między datami")


#zad 10
import datetime
z = datetime.datetime(int(input("Od którego roku: ")), 1, 1)
x = datetime.datetime(int(input("Do którego roku: ")), 1, 1)
lista = []
last = z

while z.strftime("%A") != 'Monday':
    z += datetime.timedelta(days=1)

setmonth = 0
while True:
    if z > x:
        break
    if z.strftime("%A") == 'Monday':
        if setmonth != z.strftime("%m"):
            lista.append(z.strftime("%x"))
            setmonth = z.strftime("%m")

    z += datetime.timedelta(days=1)
print(lista)