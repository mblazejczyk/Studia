from collections import Counter

def are_anagrams(s1, s2):
    # Funkcja sprawdzająca, czy dwa ciągi znaków są anagramami
    return Counter(s1) == Counter(s2)

def find_anagrams_in_file(file_path):
    anagram_pairs = []  # Tablica na pary anagramów wraz z ich indeksami

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for i in range(len(lines)):
                for j in range(i + 1, len(lines)):
                    word1 = lines[i].strip()
                    word2 = lines[j].strip()

                    if are_anagrams(word1, word2):
                        anagram_pairs.append((word1, word2, i, j))
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    return anagram_pairs

if __name__ == "__main__":
    file_path = 'anagramy.txt'  # Zastąp 'nazwa_pliku.txt' nazwą rzeczywistego pliku
    anagram_pairs = find_anagrams_in_file(file_path)

    if anagram_pairs:
        print("Znalezione pary anagramów (wraz z indeksami):")
        for pair in anagram_pairs:
            print(f"{pair[0]} (indeks {pair[2]}) - {pair[1]} (indeks {pair[3]})")
        print("Łącznie: " + str(len(anagram_pairs)))
    else:
        print("Brak par anagramów w pliku.")
