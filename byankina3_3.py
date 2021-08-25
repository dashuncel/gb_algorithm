#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

HB = random.randint(10, 25)
random_arr = [random.randint(1, 100) for i in range(1, HB)]
print(random_arr)

min_idx = random_arr.index(min(random_arr))
max_idx = random_arr.index(max(random_arr))
print(min_idx, max_idx)

random_arr[min_idx], random_arr[max_idx] = random_arr[max_idx], random_arr[min_idx]
print(random_arr)