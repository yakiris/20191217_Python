# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    my_sum = sum(my_list)
    return my_sum

result = my_func(1, 2, 3)
print(result)