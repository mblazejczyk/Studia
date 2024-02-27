def dec_to_base(n, base):
    if not 2 <= base <= 36:
        return "Błędny zakres"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n == 0:
        return "0"

    result = ""
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n //= base

    return result

decimal_number = int(input("Podaj liczbę dziesiętną: "))
base = int(input("Podaj podstawę systemu (od 2 do 36): "))

print(dec_to_base(decimal_number, base))
