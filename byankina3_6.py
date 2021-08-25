#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

HB = random.randint(10, 25)
random_arr = [random.randint(1, 20) for i in range(1, HB)]
print(random_arr)

min_idx = random_arr.index(min(random_arr))
max_idx = random_arr.index(max(random_arr))

min_idx, max_idx = min(min_idx, max_idx), max(min_idx, max_idx)
print(min_idx, max_idx)

print(sum(random_arr[min_idx + 1:max_idx]))