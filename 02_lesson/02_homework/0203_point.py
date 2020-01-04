# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

mounth = int(input('Введите число от 1 до 12: '))

if mounth >= 1 and mounth <= 12:

    # ----- > Решение через list
    my_list = ['зима', 'весна', 'лето', 'оcень']
    if mounth == 12 or mounth == 1 or mounth == 2:
        print(f'{mounth}-й месяц - это {my_list[0]}')
    elif 3 <= mounth <= 5:
        print(f'{mounth}-й месяц - это {my_list[1]}')
    elif 6 <= mounth <= 8:
        print(f'{mounth}-й месяц - это {my_list[2]}')
    else:
        print(f'{mounth}-й месяц - это {my_list[3]}')

    # ----- > Решение через dist
    my_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
               7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
    print(f'{mounth}-й месяц - это {my_dict.get(mounth)}')

else:
    print('Введенное число не входит в запрашиваемый интервал.')

