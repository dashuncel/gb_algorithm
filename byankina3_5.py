#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

HB = random.randint(10, 30)
random_arr = [random.randint(-100, 100) for i in range(1, HB)]
print(random_arr)

num = min(random_arr)
if num >= 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Число {num} в позиции {random_arr.index(num)}')
