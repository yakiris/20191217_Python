# some_text = 'qweqwe'
# f = open('my_file1.txt', 'w')
# f.write(some_text)
# f.close()
#
# #dfdf

# f = open(r'C:\Users\VANS\Desktop\gb_python_new\les_05\my_file1.txt', 'r')
# print(f.read())
# print(f.readline())
# print(f.readlines())
# f.close()

# for line in f:
#     print(line, end='')
# f.close()

# f = open('text.txt', 'w')
# print(f.closed, f.mode, f.name)

# f.write('Qwe\nQwe\nAsad\n')
# str_list = ['qwe1', 'qqwe2\n', 'qwe3']
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
#     print("РџСЂРѕРёР·РѕС€Р»Р° РѕС€РёР±РєР°!")
# finally:
#     f_obj.close()


# with open("text.txt") as f:
#     try:
#         for line in f:
#             print(line[3])
#     except IndexError:
#         print('РџСЂРѕРёР·РѕС€Р»Р° РѕС€РёР±РєР°!')
#     print(f.closed)
#
# print(f.closed)

# with open('my_file1.txt', 'a+') as f:
#     f.write('new words\n')
#     f.seek(0)
#     text = f.read()
#     print(text)
#
# f = open('text.txt', 'w')
# print('qwe')

# import os
# # os.rename('text.txt', '2.txt')
# print(os.path.exists('2.txt'))

import json

# data = {'income': {'salary': 5000, 'bonus': 500000}}
# with open('person_Vasya.json', 'w') as f:
#     json.dump(data, f)

# with open('person_Vasya.json') as f:
#     data = json.load(f)
# print(data)

import shutil
# shutil.copyfile('2.txt', r'qwe\2.txt')
# shutil.copy('1', '2')
# shutil.rmtree()
# shutil.move('','')

import argparse