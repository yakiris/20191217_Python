# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('person.txt', 'a+') as f:
    f.write(f'{input("Ваше имя: ")}\n')
    f.write(f'{input("Фамилия: ")}\n')