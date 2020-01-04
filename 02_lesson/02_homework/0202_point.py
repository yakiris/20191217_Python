# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().
my_list = []
count = int(input('Сколько элементов будет содержать список? '))

for i in range(count):
    el = input('Введите элемент в список: ')
    my_list.append(el)

if count % 2 == 0:
    el_1 = 0
    el_2 = 1
    while count > el_2:
        my_list[el_1], my_list[el_2] = my_list[el_2], my_list[el_1]
        el_1 += 2
        el_2 += 2
    print(my_list)
else:
    mem_cout = my_list[-1];
    my_list.pop()
    el_1 = 0
    el_2 = 1
    while count > el_2:
        my_list[el_1], my_list[el_2] = my_list[el_2], my_list[el_1]
        el_1 += 2
        el_2 += 2
    my_list.append(mem_cout)
    print(my_list)