#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

RC = random.randint(4, 10) #row count
CC = random.randint(4, 10) #column count
print(f'Генерируем матрицу {CC}X{RC}')

random_arr = [random.randint(1, 20) for i in range(RC)]
for i in range(len(random_arr)):
    random_arr[i] = [random.randint(1, 20) for j in range(CC)]

print(random_arr)

min_el = []
for i in range(CC):
    min_val = random_arr[0][i]
    for j in range(RC):
        min_val = min(min_val, random_arr[j][i])
    min_el.append(min_val)

print(f'Список минимальных по столбцам элементов: {min_el}')
print(f'Максимальный из минимальных по столбцам элемент равен {max(min_el)}')

