import random

def generateMatrix(m, n):
    mat = []
    for i in range(m):
        mat.append([0] * n)
    for i in range(m):
        for j in range(n):
            mat[i][j] = random.randint(1, 10)
    return mat


class Matrix:
    def __init__(self, mat_list):
        self.__mat_list = mat_list
        print(f'Constructor: matrix is {self.__mat_list}')
    def __str__(self):
        strMatrix = 'Matrix is: '
        m = len(self.__mat_list)
        for i in range(m):
            n = len(self.__mat_list[i])
            strMatrix += '\n'
            for j in range(n):
                strMatrix += str(self.__mat_list[i][j]) + '  '
        return strMatrix
    def __add__(self, other):
        m1 = len(self.__mat_list)
        m2 = len(other.__mat_list)
        m_result = generateMatrix(len(self.__mat_list), len(self.__mat_list[0]))
        if m1 != m2:
            return None
        for i in range(m1):
            n1 = len(self.__mat_list[i])
            n2 = len(other.__mat_list[i])
            if n1 != n2:
                return None
            for j in range(n1):
                m_result[i][j] = self.__mat_list[i][j] + other.__mat_list[i][j]
        return m_result


matrix_list = generateMatrix(3, 4)
print(f'Matrix list: {matrix_list}')
matrix = Matrix(matrix_list)
print(matrix)

matrix_list2 = generateMatrix(3, 4)
matrix2 = Matrix(matrix_list2)
print(f'SUM of matrix_1 and matrix_2: {matrix + matrix2}')