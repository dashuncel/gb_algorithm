# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

COUNT = 3
my_list = []


def counter(num):
    summa = 0
    while num >= 1:
        summa += num % 10
        num = num // 10
    return summa


for i in range(COUNT):
    my_list.append(int(input(f'Число {i + 1}: ')))

print(max(counter(i) for i in my_list))