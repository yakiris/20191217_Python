# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
ru_number = []
with open('number.txt') as f:
    file = f.read().splitlines()
    for i in file:
        if i == 'One - 1':
            ru_number.append('Один - 1')
        elif i == 'Two - 2':
            ru_number.append('Два - 2')
        elif i == 'Three - 3':
            ru_number.append('Три - 3')
        elif i == 'Four - 4':
            ru_number.append('Четыре - 4')

with open('ru_number.txt', 'w') as f:
    for i in ru_number:
        f.write(f'{i}\n')
