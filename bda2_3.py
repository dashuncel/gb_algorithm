# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

str_in = input('Введите натуральное число: ')
num_in = int(str_in)

# 1 вариант как с чилом:
num_out = 0
i = len(str(num_in)) - 1

while i >= 0:
   num_out = num_in % 10 * 10 ** i + num_out
   num_in = num_in // 10
   i -= 1

print(f'{str_in} -> {num_out}')

# 2 со строкой
print(str_in[::-1])