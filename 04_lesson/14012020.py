# import my_module as mm
#
# mm.my_func(20, 30)
# print(mm.pow(1, 2))

# from my_module import my_func, pow
#
# my_func(10, 50)
# print(pow(1, 2))

# from my_module import *
#
# my_func(2, 2)
# print(pow(50, 2))

# import my_module
# print(__name__)

# import time
# a = time.time() # исчисление в сек с 1970г.
# time.sleep(1)
# b = time.time()
# print(b - a)

# import math as m
# print(m.pi)
#
# from math import pi
# pi = 4
# print(pi)
#
# print(m.floor(4.5))
# print(m.ceil(4.5))

# import sys
# print(sys.path)

# import qwe.my_module as lib

# import sys
# import time
# params = sys.argv
# if 'h' in params or 'help' in params:
#     print('How to work...')
#
# else:
#     print('Coping...')
#     copy_from = params[1]
#     copy_to = params[2]
#     # копирование
#     time.sleep(2)
#
#     print(f'Copied from {copy_from} to {copy_to}')

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# new_list = [el for el in my_list if el % 2 == 0]
# new_tuple = (el for el in my_list if el % 2 == 0)
# new_dict = {el: el**2 for el in my_list if el % 2 == 0}
# print(new_list)
# print(new_tuple)
# print(new_dict)

# import random
#
# print(random.randint(0, 10))
# print(random.randrange(10, 13, 2))
# a = random.random()
#
# print('orel' if a < 0.5 else 'reshka')

# genarator = (i * i for i in range(5))
# print(list(genarator))
# print(list(genarator))
# for qwe in genarator:
#     print(qwe)
#
# for qwe in genarator:
#     print(qwe)
# print(next(genarator))

# def generator():
#     for el in (range(50)):
#         yield el
# g = generator()
#
# print(g)
#
# for el in g:
#     print(el)

# from functools import reduce
# def my_f(num1, num2):
#     return num1 + num2
# print(reduce(my_f, [10, 20, 30, 1]))

# from functools import partial
# def my_f(num1, num2):
#     return num1 * num2
# new_func = partial(my_f, 4)
# print(new_func)
# print(new_func(2))

# import itertools

# for i in itertools.count(start=0, step=1):
#     print(i)

# for el in itertools.count(7):
#     if el > 15:
#         break
#     print(el)

# from itertools import cycle
#
# c = 0
# for el in cycle('abc'):
#     if c > 10:
#         break
#     print(el)
#     c += 1

# import os
# print(os.getcwd())
# os.chdir('qwe')
# print(os.getcwd())
# os.remove()
# os.mkdir('qwe1')
# print(os.listdir())
# print(os.path.isdir('qwe'))
