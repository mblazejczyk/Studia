def is_palindrome(s):
    # Funkcja sprawdzająca, czy dany ciąg znaków jest palindromem
    s = s.lower()  # Przekształcamy ciąg znaków na małe litery
    s = ''.join(c for c in s if c.isalnum())  # Usuwamy znaki niealphanumericzne
    return s == s[::-1]

def find_palindromes_in_file(file_path):
    palindromes = []  # Tablica na palindromy

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if is_palindrome(word):
                        palindromes.append(word)
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    return palindromes

if __name__ == "__main__":
    file_path = 'palindromy.txt'  # Zastąp 'nazwa_pliku.txt' nazwą rzeczywistego pliku
    palindromes = find_palindromes_in_file(file_path)

    if palindromes:
        print("Znalezione palindromy:")
        for palindrome in palindromes:
            print(palindrome)
        print("Łącznie: " + str(len(palindromes)))
    else:
        print("Brak palindromów w pliku.")
