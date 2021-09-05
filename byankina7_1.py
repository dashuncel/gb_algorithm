'''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''
import random


def bubble_sort(arr, to=False):
    n = 1
    while n < len(arr):
        replace = False
        for i in range(len(arr) - n):
            if not to and arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                replace =True
            elif to and arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                replace = True
        if not replace:
           break
        n += 1
    print(f'Количество итераций: {n=}, Размерность массива: {len(arr)}')
    return arr


HB = random.randint(10, 30)
random_arr = [random.randint(-100, 100) for i in range(1, HB)]
print(random_arr)
print(bubble_sort(random_arr))


'''
[-76, -50, -93, 61, -33, 87, 75, 88, -99, -70, -2, 11, -4, -69, 6, -52, 15, -82, -50, 3, -95, -4, -65, -19, 56]
Количество итераций: n=21, Размерность массива: 25
[88, 87, 75, 61, 56, 15, 11, 6, 3, -2, -4, -4, -19, -33, -50, -50, -52, -65, -69, -70, -76, -82, -93, -95, -99]
'''
