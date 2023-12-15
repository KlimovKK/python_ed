#  Шахматная доска
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())

matrix = [['*'] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = '.'
        else:
            matrix[i][j] = '*'

print_matrix(matrix, n, m)


#  Побочная диагональ
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            matrix[i][j] = 1
        elif i + j > n - 1:
            matrix[i][j] = 2

print_matrix(matrix, n, n)


#  Заполнение 1
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())

matrix = []
for i in range(1, n + 1):
    tmp = list(range(m * i - m + 1, m * i + 1))
    matrix.append(tmp)

print_matrix(matrix, n, m, width=3)


#  Заполнение 2
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = j * n + i + 1

print_matrix(matrix, n, m, width=3)
