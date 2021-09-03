# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = input("Введите число: ")
summa = 0
comp = 1

for i in str(number):
   summa += int(i)
   comp *= int(i)

print(f'Произведение цифр числа {number} = {comp}')
print(f'Сумма цифр числа {number} = {summa}')