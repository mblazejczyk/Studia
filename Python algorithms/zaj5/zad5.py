def base_to_dec(number, base):
    if not 2 <= base <= 36:
        return "Podstawa systemu powinna być w zakresie od 2 do 36."

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = str(number).upper()

    decimal_number = 0
    power = 0

    for digit in reversed(number):
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit) - ord('A') + 10

        decimal_number += digit_value * (base ** power)
        power += 1

    return decimal_number

def dec_to_base(n, base):
    if not 2 <= base <= 36:
        return "Podstawa systemu powinna być w zakresie od 2 do 36."

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n == 0:
        return "0"

    result = ""
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n //= base

    return result

number = input("Podaj liczbę: ")
current_base = int(input("Podaj obecną podstawę systemu (od 2 do 36): "))
target_base = int(input("Podaj docelową podstawę systemu (od 2 do 36): "))

if current_base != 10:
    decimal_number = base_to_dec(number, current_base)
else:
    decimal_number = int(number)

print(dec_to_base(decimal_number, target_base))
