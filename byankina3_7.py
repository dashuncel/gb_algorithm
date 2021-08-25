#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

HB = random.randint(10, 25)
random_arr = [random.randint(1, 20) for i in range(1, HB)]
print(random_arr)

sorted_arr = sorted(random_arr)
print(f'Наименьшие элементы {sorted_arr[0]} и {sorted_arr[1]}')
