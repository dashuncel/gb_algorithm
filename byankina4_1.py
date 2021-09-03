'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

import cProfile


def get_summ(n):
    if n < 1:
        return 0
    else:
        return n + get_summ(n - 1)


def get_summ2(n):
    return sum(range(int(n)+1))


def get_summ3(n):
   i = 0
   summa = 0
   while i < n:
       i += 1
       summa += i
   return summa


def run_all(n):
    print(get_summ(50))
    print(get_summ2(n))
    print(get_summ3(n))


run_all(100000000)

pr = cProfile.Profile()
pr.enable()
cProfile.run(run_all(1000))

'''
скорость:
        1    0.000    0.000    8.777    8.777 byankina4_1.py:1(<module>)
        1    0.000    0.000    2.702    2.702 byankina4_1.py:14(get_summ2)
        1    6.073    6.073    6.073    6.073 byankina4_1.py:17(get_summ3)
        1    0.000    0.000    8.776    8.776 byankina4_1.py:26(run_all)
    101/1    0.000    0.000    0.000    0.000 byankina4_1.py:8(get_summ)
    
Сложность: get_summ() = O(n**2)
           get_summ2() = O(n)
           get_summ3() = O(n)
'''


