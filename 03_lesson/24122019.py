# print()
# input()
# max()
# min()

# print(max(1, 2, 3))
# print(max('zz', 'aaa', key=len))
# print(round(1.987654231, 4))

# def say_hello(data):
#     print('Hi,', data)
#
# name = input('Name: ')
# say_hello(name)

# def average(numbers):
#     count = len(numbers)
#     my_sum = sum(numbers)
#     result = my_sum / count
#     return result
#
#
# out = average([1, 2, 3, 4, 5])
# print(out)

# def print(text):
#     pass
#
# print('bla')

# x = 100
# def test(x):
#     x = 99
#     return x
#
# x = test(x)
# print(x)

# def function(name, surname='Guest'):
#     print(name, surname)
#
# function('Ivan', 'Ivanov')


def function(name, na, *args):
    print(name, args, na)


#
# function('Ivan', 'Ivanov', 20, 50)

# def function(name, age, surname):
#     print(name, age, surname)
#
# function(age=20, name='Ivan', surname='Ivanov')

# def func(name, **kwargs):
#     print(name, kwargs)
# func('Ivan', age=20, surname='Ivanov')

# names = ['Ivan', 'Engeniy', 'Alexander']
# ages = [27, 35, 78, 50]
#
# print(list(zip(names, ages)))
# print(dict(zip(names, ages)))

# def my_pow(x):
#     return x ** 2


data = [-1, -2, -3, 1, 2, 3]

# result = []
# for i in data:
#     result.append(my_pow(i))
# print(result)

# result = list(map(my_pow, data))
# print(result)

# def my_filter(x):
#     return x > 0
#
# result = list(filter(my_filter, data))
# print(result)


# result = list(map(lambda x: x ** 3 - 5, data))
# print(result)

result = list(filter(lambda x: x > 0, data))
print(result)
