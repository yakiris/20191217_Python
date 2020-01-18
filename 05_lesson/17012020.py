# f = open('my_file.txt')
# file = f.read()
# print(file)
# f.close()

# some_text = 'qweqwe'
# f = open('my_file1.txt', 'w')
# f.write(some_text)
# f.close()

# f = open(r'D:\Project_Data_Science\20191217_Основы_Python\05_lesson\my_file1.txt', 'r')
# print(f.read()) # выводит весь текст
# print(f.readline()) # выводит строку до \n
# print(f.readlines()) # выводит все строки в список, элемент списка до \n
# f.close()

# for line in f:
#     print(line, end='')
# f.close()

# f.write('Qwe\nQwe\nAsad\n')
# str_list = ['qwe1', 'qwe2\n', 'qwe3\n']
# f.writelines(str_list)
# f.close()

# with open('my_file1.txt') as f:
#     for line in f:
#         print(line, end='')

# try:
#     f_obj = open("text.txt")
#     for line in f_obj:
#         print(line[3])
# except IndexError:
#     print("Произошла ошибка!")
# finally:
#     f_obj.close()

# with open("text.txt") as f:
#     try:
#         for line in f:
#             print(line[3])
#     except IndexError:
#         print('Произошла ошибка!')
#     print(f.closed)
# print(f.closed)

# f = open('text.txt', 'w')
# print(f.closed, f.mode, f.name)

# with open('my_file1.txt', 'a+') as f:
#     print(f.tell())
#     f.write('new words\n')
#     print(f.tell())
#     f.seek(0)
#     text = f.read()
#     print(text)
#
# with open('text.txt', 'w') as f:
#     print('qwe', file = f)

# import os
# os.rename('text.txt', '2.txt')
# print(os.path.exists('2.txt')) # поиск наличия файла

# import json

# data = {'income': {'salary': 5000, 'bonus': 500000}}
# with open('person_Vasya.json', 'w') as f:
#     json.dump(data, f)

# with open('person_Vasya.json') as f:
#     data = json.load(f)
# print(data)

# import shutil
# shutil.copyfile('2.txt', r'qwe\2.txt')
# shutil.copy('1', 'qwe')
# shutil.rmtree()
# shutil.move('','')

import argparse