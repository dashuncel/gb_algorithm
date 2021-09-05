'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
'''
import random

HB = 13
random_arr = [random.randint(0, 50) for i in range(1, HB + 1)]
print(random_arr)
#random_arr = [5, 29, 30, 44, 48, 34, 2, 11, 4, 22, 29, 26, 30 ] # test-case медиана = 29 повторяется

for i in range(len(random_arr)):
    less = 0
    more = 0
    for j in range(len(random_arr)):
        if i == j:
            continue
        if random_arr[j] < random_arr[i]:
            less += 1
        if random_arr[j] >= random_arr[i]:
            more += 1
    print(f'{random_arr[i]}: {less =}, {more =}')

    if less == more:
        print(f'Медиана:{random_arr[i]}, итераций {i}')
        break

'''
Results:

[35, 42, 13, 34, 37, 49, 50, 41, 18, 2, 33, 46, 12]
35: less =6, more =6
Медиана:35, итераций 0

[44, 49, 35, 40, 10, 34, 17, 23, 24, 6, 28, 2, 17]
44: less =11, more =1
49: less =12, more =0
35: less =9, more =3
40: less =10, more =2
10: less =2, more =10
34: less =8, more =4
17: less =3, more =9
23: less =5, more =7
24: less =6, more =6
Медиана:24, итераций 8
'''

