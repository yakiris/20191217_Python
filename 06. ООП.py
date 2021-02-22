task = int(input('Запустить задачу номер: '))
if task == 1:
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.
    import time

    class TrafficLight():
        def __init__(self):
            self.__color = 0

        def running(self, color):
            if color == 'red' and self.__color == 0:
                print('Горит красный')
                time.sleep(7)
                self.__color = 1
            elif color == 'yellow' and self.__color == 1:
                print('Горит желтый')
                time.sleep(2)
                self.__color = 2
            elif color == 'green' and self.__color == 2:
                print('Горит зеленый')
                time.sleep(10)
                self.__color = 0
            else:
                print('Нарушен порядок режимов')

    traf = TrafficLight()
    order = ['red', 'yellow', 'green', 'red', 'green']
    for i in order:
        traf.running(i)

elif task == 2:
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
    length = int(input('Длина дорожного полотна м: '))
    width = int(input('Ширина м: '))
    thick = int(input('Толщина см.: '))

    class Road:
        def __init__(self, length, width, thick):
            self._length = length
            self._width = width
            self.thick = thick

        def calcul(self, mass = 25/1000):
            total = self._length * self._width * mass * self.thick
            print(f'Необходимо {total} т асфальта')

    my_road = Road(length, width, thick)
    my_road.calcul()

elif task == 3:
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

    my_dict = {'ware': 80000, 'bonus': 25000}

    class Worker:
        def __init__(self, name, surname, position, my_dict):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = my_dict

    class Position(Worker):
        def get_full_name(self):
            full_name = f'{self.name} {self.surname} - {self.position}'
            print(full_name)

        def get_total_income(self):
            total_income = sum(self._income.values())
            print(total_income)

    position = Position('Ivan', 'Ivanov', 'programmer', my_dict)
    position.get_full_name()
    position.get_total_income()

elif task == 4:
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

    class Car:
        def __init__(self, speed, color, name, is_police):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police

        def go(self):
            print('Car go')

        def stop(self):
            print('Car stop')

        def turn(self):
            print('Car turn')

        def show_speed(self):
            print(f'Скорось {self.name} цвета {self.color}  - {self.speed}.')

    class TownCar(Car):

        def show_speed(self):
            if self.speed > 60:
                print(f'{self.name} цвета {self.color}! Превышение скорости!')
            else:
                print(f'Скорось {self.name} цвета {self.color}  - {self.speed}.')

    class SportCar(Car):
        pass

    class WorkCar(Car):
        def show_speed(self):
            if self.speed > 40:
                print(f'{self.name} цвета {self.color}! Превышение скорости!')
            else:
                print(f'Скорось {self.name} цвета {self.color}  - {self.speed}.')

    class PoliceCar(Car):
        pass

    tc = TownCar(40, 'white', 'Town', True)
    tc.show_speed()
    sc = SportCar(150, 'red', 'Sport', True)
    sc.show_speed()
    wc = WorkCar(60, 'green', 'Work', False)
    wc.show_speed()
    pc = PoliceCar(200, 'black', 'Police', False)
    pc.show_speed()

elif task == 5:
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.
    class Stationery:
        def __init__(self, title):
            self.title = title

        def draw(self):
            print('Запуск отрисовки')

    class Pen(Stationery):
        def draw(self):
            print(f'Запуск отрисовки {self.title}')

    class Pencil(Stationery):
        def draw(self):
            print(f'Запуск отрисовки {self.title}')

    class Handle(Stationery):
        def draw(self):
            print(f'Запуск отрисовки {self.title}')

    pen = Pen('ручкой')
    pen.draw()
    pencil = Pencil('карандашом')
    pencil.draw()
    handle = Handle('маркером')
    handle.draw()

