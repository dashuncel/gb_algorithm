#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

num = int(input('Введите число элементов ряда: '))
my_list = [1]

for i in range(1, num):
    my_list.append(my_list[i-1] * -1 / 2)
print(my_list)

print(f'Сумма чисел ряда: {sum([i for i in my_list])}')
