#2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), # т.к. именно в этих позициях первого массива стоят четные числа.
import random

HB = random.randint(1, 20)
first_arr = [random.randint(1, 100) for i in range(1, HB)]
print(first_arr)
second_arr = [key for key, elem in enumerate(first_arr) if elem % 2 == 0]
print(second_arr)

