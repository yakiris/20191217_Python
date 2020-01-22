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
        self._color = 0

    def running(self, color):
        if color == 'red' and self._color == 0:
            print('Горит красный')
            time.sleep(7)
            self._color = 1
        elif color == 'yellow' and self._color == 1:
            print('Горит желтый')
            time.sleep(2)
            self._color = 2
        elif color == 'green' and self._color == 2:
            print('Горит зеленый')
            time.sleep(10)
            self._color = 0
        else:
            print('Нарушен порядок режимов')

traf = TrafficLight()
traf.running('red')
traf.running('yellow')
traf.running('green')
traf.running('red')
traf.running('green')

