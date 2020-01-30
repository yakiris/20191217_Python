# class Car:
#     def __init__(self):
#         self.modules = []
#         self.f_c = 7
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):
#         return 'Авто с модулями:' + ", ".join(self.modules)
#
#     def __del__(self):
#         print('Объект удален')
#

#     def __setattr__(self, key, value):
#         # print('Добавляю по ключу', key, 'Рзначение', value)
#         # super().__setattr__(key, value)
#         self.__dict__[key] = value
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price = None):
#         print(f'Машина {self.model}, модули {self.modules}, цена {price}')
#
#     def __eq__(self, other):
#         return self.f_c == other
#
# my_car = Car()
# my_car + 'теплый руль'
# my_car + 'подогрев стекла'
# my_car + 'теплый пол'
#
# my_car.model = 'Tesla'
# print(my_car.model)
#
# print(my_car[1])
# my_car(5000)
# print('Равно' if my_car == 7 else 'Не равно')

# class Auto:
#     def fuel_c(self, f_c):
#         self.f_c = f_c
#         print('Расход: ', f_c, 'л/100')
#
# class EAuto(Auto):
#     def fuel_c(self, f_c):
#         self.f_c = f_c
#         print('Расход: ', f_c, 'кв/ч')

# from abc import ABC, abstractmethod
#
# class MyAbcMethod(ABC):
#     @abstractmethod
#     def my_method_1(self):
#         pass
#
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
# class MyClass(MyAbcMethod):
#     def my_method_1(self):
#         pass
#
#     def my_method_2(self):
#         pass
#
# mc = MyClass()

# for i in [1, 2, 3, 4]:
#     print(i)

# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i < 6:
#             return self.i
#         else:
#             raise StopIteration
#
# qwe = Iterator()
#
# for i in qwe:
#     print(i)

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.sex = sex

    @property
    def age(self):
        if self._age < 0:
            self._age = 0
        return self._age

# много кода
human = Human('Alex', 20, 'м')
print(human.age)
