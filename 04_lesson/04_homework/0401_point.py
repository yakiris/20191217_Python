# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
params = sys.argv

def calc(hour, salary, premium):
    result = (hour * salary) + premium
    return result

if len(params) == 0:
    print('Введите параметры расчета')
else:
    hour = params[1]
    salary = params[2]
    premium = params[3]
    print(f'Заработная плата сотрудника: {calc(int(hour), int(salary), int(premium))}')