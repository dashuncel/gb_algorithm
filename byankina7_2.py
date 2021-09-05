'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    a1 = merge_sort(arr[:middle])
    a2 = merge_sort(arr[middle:])

    i1 = i2 = 0
    result = []

    while i1 < len(a1) or i2 < len(a2):
        if i1 >= len(a1):
            result.append(a2[i2])
            i2 += 1
        elif i2 >= len(a2):
            result.append(a1[i1])
            i1 += 1
        elif a1[i1] <= a2[i2]:
            result.append(a1[i1])
            i1 += 1
        elif a2[i2] < a1[i1]:
            result.append(a2[i2])
            i2 += 1
    return result


HB = random.randint(10, 30)
random_arr = [random.randint(0, 50) for i in range(1, HB)]
print(random_arr)
print(merge_sort(random_arr))

#[38, 23, 37, 14, 5, 7, 49, 47, 33, 16, 22, 8, 39, 44, 4]
#[4, 5, 7, 8, 14, 16, 22, 23, 33, 37, 38, 39, 44, 47, 49]
