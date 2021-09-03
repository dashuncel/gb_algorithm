#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

DELTA = 64

letter1 = input("Введите 1 букву английского алфавита (1-26): ").capitalize()
letter2 = input("Введите 2 букву английского алфавита (1-26): ").capitalize()
print(f'Между буквами {letter1} и {letter2} - {abs(ord(letter1) - ord(letter2)) - 1} букв')
print(f'Буква {letter1} по счету - {ord(letter1) - DELTA}, буква {letter2} - {ord(letter2) - DELTA}')