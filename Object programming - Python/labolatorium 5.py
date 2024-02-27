#Mateusz Błażejczyk
#zad 2
try:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    wynik = liczba1 / liczba2
    print("Wynik dzielenia: ", wynik)

except ZeroDivisionError:
    print("Błąd: Druga liczba nie może być zerem!")





#zad 3
try:
    liczba = int(input("Podaj liczbę całkowitą: "))
    print("Wprowadzona liczba:", liczba)

except ValueError:
    print("Błąd: Wprowadzona wartość nie jest liczbą całkowitą!")





#zad 4
try:
    nazwa_pliku = input("Podaj nazwę pliku: ")
    with open(nazwa_pliku, 'r') as plik:
        zawartosc = plik.read()
        print("Zawartość pliku:")
        print(zawartosc)

except FileNotFoundError:
    print("Błąd: Plik nie istnieje!")





#zad 5
try:
    nazwa_pliku = input("Podaj nazwę pliku: ")
    with open(nazwa_pliku, 'r') as plik:
        zawartosc = plik.read()
        print("Zawartość pliku:")
        print(zawartosc)

except FileNotFoundError:
    print("Błąd: Plik nie istnieje!")

except PermissionError:
    print("Błąd: Brak uprawnień do odczytu pliku!")





#zad 6
class DivideByZeroError(Exception):
    pass


def divide_elements(lista):
    wyniki = []
    for element in lista:
        try:
            wynik = 1 / element
            wyniki.append(wynik)
        except ZeroDivisionError:
            raise DivideByZeroError("Błąd: Dzielenie przez zero!")

    return wyniki


lista_danych = [2, 1, 4, 6, 1, 8]
wyniki_dzielenia = divide_elements(lista_danych)
print("Wyniki dzielenia:", wyniki_dzielenia)






#zad 7
oceny_uczniow = {
    'Jan Kowalski': 4.5,
    'Anna Nowak': 5.0,
    'Piotr Nowicki': 3.5,
    'Maria Wiśniewska': 4.0
}

nazwisko = input("Podaj nazwisko ucznia: ")

try:
    ocena = oceny_uczniow[nazwisko]
    print("Ocena ucznia", nazwisko, "to:", ocena)
except KeyError:
    print("Błąd: Brak oceny dla podanego nazwiska ucznia.")







#zad 8
lista_liczb = input("Podaj listę liczb (oddzielone spacjami): ").split()
indeks = int(input("Podaj indeks elementu do wyświetlenia: "))

try:
    element = lista_liczb[indeks]
    print("Element o indeksie", indeks, "to:", element)
except IndexError:
    print("Błąd: Podany indeks jest poza zakresem.")






#zad 9
import math

class NegativeNumberError(Exception):
    pass

def oblicz_pierwiastek_kwadratowy(liczba):
    if liczba < 0:
        raise NegativeNumberError("Błąd: Podano liczbę ujemną!")
    else:
        return math.sqrt(liczba)

try:
    liczba = float(input("Podaj liczbę dodatnią: "))
    pierwiastek = oblicz_pierwiastek_kwadratowy(liczba)
    print("Pierwiastek kwadratowy z", liczba, "to:", pierwiastek)
except ValueError:
    print("Błąd: Podano niepoprawną liczbę!")
except NegativeNumberError as e:
    print(e)





#zad 10
try:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    wynik = liczba1 / liczba2
    print("Wynik dzielenia:", wynik)
except ValueError:
    print("Błąd: Podano niepoprawną liczbę!")
except ZeroDivisionError:
    print("Błąd: Dzielenie przez zero!")
except NameError:
    print("Błąd: Niedefiniowana zmienna!")
    
    
    
    
    
#zad 11
try:
    with open("/home/nibek1000/lab5/test.txt", "r") as plik:
        zawartosc = plik.read()
        print("Zawartość pliku:", zawartosc)
except FileNotFoundError:
    print("Błąd: Plik nie istnieje!")
except IOError:
    print("Błąd wejścia/wyjścia podczas odczytu pliku!")
else:
    print("Operacje na pliku wykonane bez błędów.")
finally:
    print("Zamykanie pliku.")
    
    
    
    
    
    
#zad 12
import csv

try:
    with open("/home/nibek1000/lab5/dane_uczniow.csv", "r") as plik:
        plik_csv = csv.reader(plik)
        for wiersz in plik_csv:
            try:
                imie = wiersz[0]
                nazwisko = wiersz[1]
                wiek = int(wiersz[2])

                print("Imię:", imie)
                print("Nazwisko:", nazwisko)
                print("Wiek:", wiek)
                print("-------------------")
            except IndexError:
                print("Błąd: Niepoprawny format danych w pliku.")
                continue
            except ValueError:
                print("Błąd: Niepoprawny format wieku ucznia.")
                continue
except FileNotFoundError:
    print("Błąd: Plik nie istnieje!")
except IOError:
    print("Błąd wejścia/wyjścia podczas odczytu pliku!")