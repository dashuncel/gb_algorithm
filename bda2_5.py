#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

col = 0
for i in range(32, 128):
    col += 1
    if col % 10 == 0:
        end_str = '\n'
    else:
        end_str = '\t'

    print(f'{i} - {chr(i)}', end = end_str)
