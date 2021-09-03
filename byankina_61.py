'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
'''
import sys
import random
import platform
from memory_profiler import profile

print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}') #Python 3.9.7
print(f'OS {platform.architecture() = }') #('64bit', 'WindowsPE')

#3.9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
def first_sample():
    print('-' * 20)
    RC = random.randint(4, 20) #row count
    CC = random.randint(4, 10) #column count
    print(f'Генерируем матрицу {CC}X{RC}')
    '''
    Для int RC, CC всегда 28 bytes. 
    для матрицы:
    9x5 matrix sys.getsizeof(random_arr) = 120 bytes
    4x10 matrix sys.getsizeof(random_arr) = 184 bytes
    4x7 matrix sys.getsizeof(random_arr) = 120 bytes
    9x8 matrix sys.getsizeof(random_arr) = 120 bytes
    9x17 matrix sys.getsizeof(random_arr) = 248 bytes                       
    '''

    random_arr = [random.randint(1, 20) for i in range(RC)]
    for i in range(len(random_arr)):
        random_arr[i] = [random.randint(1, 20) for j in range(CC)]

    print(f'{CC}x{RC} matrix {sys.getsizeof(random_arr) = } bytes')
    print(random_arr)

    min_el = []
    for i in range(CC):
        min_val = random_arr[0][i]
        for j in range(RC):
            min_val = min(min_val, random_arr[j][i])
        min_el.append(min_val)
    print(f'Список минимальных по столбцам элементов: {min_el}')
    print(f'Максимальный из минимальных по столбцам элемент равен {max(min_el)}')


def second_sample():
    #3.1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
    my_dict = {a: 0 for a in range(2, 10)}
    for key in my_dict.keys():
        for i in range(int(key), 100, int(key)):
            my_dict[key] += 1
    print(my_dict)
    print(f'DICT {sys.getsizeof(my_dict) = } bytes')
    '''
    {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
    DICT sys.getsizeof(my_dict) = 360 bytes
    '''

first_sample()
second_sample()
