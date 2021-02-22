task = int(input('Запустить задачу номер: '))
if task == 1:
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
    with open('data/person.txt', 'w') as f:
        while True:
            line = input('Введите строку: ')
            if line == '':
                break
            f.write(line + '\n')

elif task == 2:
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
    with open('data/text.txt') as f:
        lines = f.readlines()
        print(f'В файле - {len(lines)} строк(и)')
        for line, word in enumerate(lines, start=1):
            print(f"В строке {line} - {len(word.split(' '))} слов(а)")

elif task == 3:
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
    import codecs

    my_dict = {}
    with codecs.open('data/salary.txt', 'r', 'utf-8') as f:
        file = f.read().splitlines()
        for i in file:
            line = i.split(' ')
            my_dict[line[0]] = float(line[1])

    print('Сотрудники с окладом менее 20 тысяч:')
    for name, salary in my_dict.items():
        if salary < 20000.00:
            print(name, salary)

    print(f'Средний доход всех сотрудников: {round(sum(my_dict.values())/len(my_dict.keys()), 2)}')

elif task == 4:
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
    ru_number = []
    with open('data/number.txt') as f:
        file = f.read().splitlines()
        trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        for i in file:
            temp = i.split()
            temp[0] = trans[i.split()[0]]
            ru_number.append(' '.join(temp))

    with open('data/ru_number.txt', 'w') as f:
        for i in ru_number:
            f.write(f'{i}\n')

    with open('data/ru_number.txt') as f:
        print(f.read())

elif task == 5:
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    with open('data/numbers.txt', 'w+') as f:
        f.write('1 2 3 4 5 6 7 8 9 10')
        f.seek(0)
        num = f.read().split()
        total = sum(map(int, num))
        print(f'Сумма чисел из файла = {total}')

elif task == 6:
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
    my_dict = dict()
    with open('data/lesson.txt') as f:
        lines = f.readlines()
        for line in lines:
            string = line.split()
            subject = string[0]
            sum_num = sum([int(x[:x.find('(')]) for x in string[1:] if '(' in x])
            my_dict[subject[:-1]] = sum_num
    print(my_dict)

elif task == 7:
# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
    import json

    my_firm = {}
    av_prof = []
    with open('data/firm.txt') as f:
        lines = f.read().splitlines()
        for i in lines:
            name, form, revenue, costs = i.split()
            prof = int(revenue) - int(costs)
            my_firm[name] = prof
            if prof > 0:
                av_prof.append(prof)
    av_prof = sum(av_prof)/len(av_prof)
    out_info = [my_firm, {'average_profit':av_prof}]

    with open('data/firm.json', 'w') as f:
        json.dump(out_info, f)