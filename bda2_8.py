# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

numeral = input('Введите цифру, которую ищем: ')
count = int(input('Введите размер ряда: '))
my_list = []

for i in range(count):
    my_list.append(int(input(f'Число {i + 1}: ')))

str = ''.join(str(i) for i in my_list)

print(f'Количество вхождений цифры {numeral} в ряду {my_list}: {str.count(numeral)}')