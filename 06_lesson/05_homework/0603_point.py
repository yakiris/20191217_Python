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
        full_name = f'{self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(total_income)

position = Position('Ivan', 'Ivanov', 'programmer', my_dict)
position.get_full_name()
position.get_total_income()
