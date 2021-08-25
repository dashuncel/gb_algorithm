#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


my_dict = {a: 0 for a in range(2, 10)}
for key in my_dict.keys():
    for i in range(int(key), 100, int(key)):
        my_dict[key] += 1

print(my_dict)

