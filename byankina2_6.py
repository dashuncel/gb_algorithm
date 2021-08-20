#6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

EQ = 'equal'
LT = 'меньше'
GT = 'больше'
NUM_TRY = 10

def where_is_num(quest, num):
    if quest == num:
        return EQ
    elif num > quest:
        return GT
    else:
        return LT


quest = random.randint(0, 100)
user_try = 0
print('Число от 0 до 100 загадано!')

while user_try < NUM_TRY:
    user_try += 1
    user_num = int(input(f'Попытка {user_try}: '))
    user_result = where_is_num(quest, user_num)

    if user_result == EQ:
        print('Поздравляю, вы победили!')
        break
    else:
        print(f'{user_num} {user_result} загаданного числа')
        if user_try == NUM_TRY:
            print('Вы проиграли, сожалею')
            break

