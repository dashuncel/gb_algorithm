#4. Определить, какое число в массиве встречается чаще всего.
import random

HB = random.randint(10, 25)
random_arr = [random.randint(1, 20) for i in range(1, HB)]
print(random_arr)

num = max(random_arr, key=random_arr.count)
print(f'число {num} встречается в массиве {random_arr.count(num)} раз')
