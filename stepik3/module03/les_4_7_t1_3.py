#  Сложение матриц
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix_1 = [[int(num) for num in input().split()] for _ in range(n)]
input()
matrix_2 = [[int(num) for num in input().split()] for _ in range(n)]
result_matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]

print_matrix(result_matrix, n, m)

#  Умножение матриц
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix_1 = [[int(num) for num in input().split()] for _ in range(n)]
input()
m, k = (int(i) for i in input().split())
matrix_2 = [[int(num) for num in input().split()] for _ in range(m)]
result_matrix = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for g in range(m):
            result_matrix[i][j] += matrix_1[i][g] * matrix_2[g][j]

print_matrix(result_matrix, n, k)


#  Возведение матрицы в степень
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def multiplies_matrices(matrix_1, matrix_2, n: int, k: int, m: int):
    """
    Умножает 2 матрицы
    :param matrix_1: первая матрица
    :param matrix_2: вторая матрица
    :param n: кол-во строк в первой матрице
    :param k: кол-во столбцов во второй матрице
    :param m: кол-во столбцов в первой и строк во второй матрицах
    :return: результирующая матрица
    """
    result_matrix = [[0] * k for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for g in range(m):
                result_matrix[i][j] += matrix_1[i][g] * matrix_2[g][j]

    return result_matrix


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
m = int(input())

result_matrix = multiplies_matrices(matrix, matrix, n, n, n)
for _ in range(m - 2):
    result_matrix = multiplies_matrices(result_matrix, matrix, n, n, n)

print_matrix(result_matrix, n, n)
