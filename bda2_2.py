#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него
# 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def my_odd(num):
    return int(num) % 2


number1 = input('Введите натуральное число: ')
counter = [0, 0]
for i in number1:
    counter[my_odd(i)] += 1

print(f'В числе {number1} {counter[0]} четных и {counter[1]} нечетных цифр')

