# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

my_list = []

my_list.append(int(input("Введите число 1: ")))
my_list.append(int(input("Введите число 2: ")))
my_list.append(int(input("Введите число 3: ")))

print(sorted(my_list)[1])
