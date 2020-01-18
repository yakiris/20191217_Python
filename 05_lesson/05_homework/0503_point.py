# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import codecs

my_dict = {}

with codecs.open('salary.txt', 'r', 'utf-8') as f:
    file = f.read().splitlines()
    for i in file:
        line = i.split(' ')
        my_dict[line[0]] = float(line[1])

print('Сотрудники с окладом менее 20 тысяч:')
for name, salary in my_dict.items():
    if salary < 20000.00:
        print(name, salary)

print(f'Средний доход сотрудников: {round(sum(my_dict.values())/len(my_dict.keys()), 2)}')