'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить
в виде комментариев в файле с кодом.
'''


def eratosphen(n=8):
    num_list = list(range(2, n + 1))
    for element in num_list:
        if element != 0:
            for n in range(2 * element, n + 1, element):
                num_list[n - 2] = 0
    return list(filter(lambda x: x != 0, num_list))


def no_eratosphen(n=8):
    num_list = []
    for x in range(2, n + 1):
        a = True
        for y in range(1, n):
            if x > y and y != 1:
                if x % y == 0:
                    a = False
                    break
        if a == True:
            num_list.append(x)

    return num_list


print(eratosphen(10000))
print(no_eratosphen(10000))

'''
Эратосфен на больши числах более быстрый.

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.547    0.547 byankina4_2.py:1(<module>)
        1    0.003    0.003    0.003    0.003 byankina4_2.py:10(eratosphen) - O(log(n))
     9999    0.001    0.000    0.001    0.000 byankina4_2.py:16(<lambda>)
        1    0.542    0.542    0.542    0.542 byankina4_2.py:19(no_eratosphen) - o(n**2)
        1    0.000    0.000    0.547    0.547 {built-in method builtins.exec}
        2    0.002    0.001    0.002    0.001 {built-in method builtins.print}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''