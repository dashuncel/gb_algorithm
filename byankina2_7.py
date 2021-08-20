#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

num = int(input('Введите натуральное число: '))
if num < 0 or not isinstance(num, int):
    print('Неверное число')
    exit(0)

def get_summ(n):
    if n < 1:
        return 0
    else:
        return n + get_summ(n - 1)

print(f'Сумма 1..{num}: {get_summ(num)}, n(n+1)/2 = {num * (num + 1) / 2}')