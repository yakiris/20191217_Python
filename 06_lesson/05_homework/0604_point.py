# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
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