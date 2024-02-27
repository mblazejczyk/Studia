#Mateusz Błażejczyk
zad 2
a = int(input("Podaj liczbe całkowitą: "))
if a < 0:
    print(a - 2*a)
else:
    print(a)


zad 3
a = int(input("Podaj liczbe: "))
if a > 100:
    print("Liczba jest większa od 100")
elif a < 0:
    print("Liczba jest mniejsza od 0")
else:
    print("Liczba jest w przedziale między 0 a 100")



zad 4
a = input("Podaj liczbe: ")
if a.isnumeric():
    b = int(a)
    match b:
        case 1:
            print(a)
        case 2:
            print(a)
        case 3:
            print(a)
        case 4:
            print(a)
        case 5:
            print(a)
        case 6:
            print(a)
        case 7:
            print(a)
        case 8:
            print(a)
        case 9:
            print(a)
        case 0:
            print(a)
        case _:
            print("Wprowadzono niepoprawne wartości")
else:
    print("Wprowadzono niepoprawne wartości")



zad 5
a = input("Czy jest piękny dzień?(t/n): ")

match a:
    case "t":
        print("Piękny dzień")
    case "T":
        print("Piękny dzień")
    case "n":
        print("Brak słóńca")
    case "N":
        print("Brak słońca")
    case _:
        print("Niepoprawne dane")




zad 6
a = input("Podaj dzień tygodnia: ").upper()
# dzięki sprawieniu że cała odpowiedź jest z wielkich liter wykluczam możliwośc różnych rodzajów wpisów
match a:
    case "PONIEDZIAŁEK":
        print("Dziś jest " + a)
    case "WTOREK":
        print("Dziś jest " + a)
    case "ŚRODA":
        print("Dziś jest " + a)
    case "CZWARTEK":
        print("Dziś jest " + a)
    case "PIĄTEK":
        print("Dziś jest " + a)
    case "SOBOTA":
        print("Dziś jest " + a)
    case "NIEDZIELA":
        print("Dziś jest " + a)
    case _:
        print("Prowadzono błędne dane")




zad 7
a = int(input("Podzaj numer indeksu: "))

if a >= 10000:
    if(a % 2) == 0:
        print("Stdent rozpoczął studia w 2019 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2019 i jest kobietą")
if a < 10000 and a >= 9000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2018 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2018 i jest kobietą")
if a < 9000 and a >= 8000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2017 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2017 i jest kobietą")
if a < 8000 and a >= 7000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2016 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2016 i jest kobietą")
if a < 7000 and a >= 6000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2015 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2015 i jest kobietą")
if a < 6000 and a >= 5000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2014 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2014 i jest kobietą")
if a < 5000 and a >= 4000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2013 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2013 i jest kobietą")
if a < 4000 and a >= 3000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2012 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2012 i jest kobietą")
if a < 3000 and a >= 2000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2011 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2011 i jest kobietą")
if a < 2000 and a >= 1000:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2010 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2010 i jest kobietą")
if a < 1000 and a >= 0:
    if (a % 2) == 0:
        print("Stdent rozpoczął studia w 2009 i jest mężczyzną")
    else:
        print("Stdent rozpoczął studia w 2009 i jest kobietą")
if a <= 0:
    print("Podano niepoprawne dane")



zad 8
print("Twoje równanie ma taki wzór: ax^2+bx+c=0")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = pow(b, 2) - 4 * a * c
print("Delta wynosi" + str(delta))
if delta > 0:
    x1 = (b * (-1) - delta) / (2 * a)
    x2 = (b * (-1) + delta) / (2 * a)
    print("x1 wynosi " + str(x1) + " a x2 wynosi " + str(x2))
elif delta == 0:
    x1 = (b * (-1) - delta) / (2 * a)
    print("x1/x2 wynosi " + str(x1))
else:
    print("Brak pierwiastków rzeczywistych")