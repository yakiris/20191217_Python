# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix():
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, line)) for line in self.my_matrix)

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.my_matrix)): new_matrix.append(list(map(lambda x, y: x + y, self.my_matrix[i], other.my_matrix[i])))
        return new_matrix

line1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
line2 = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]
matrix1 = Matrix(line1)
matrix2 = Matrix(line2)
sum_matrix = matrix1 + matrix2
matrix3 = Matrix(sum_matrix)

print(f'Первая матрица:\n{matrix1}')
print(f'Вторая матрица:\n{matrix2}')
print(f'Сумма матриц:\n{matrix3}')