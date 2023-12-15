#  Заполнение 3
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1

print_matrix(matrix, n, n, width=3)


#  Заполнение 4
def is_null(inx_1, inx_2, num):
    return inx_2 < inx_1 < num - 1 - inx_2 or num - 1 - inx_2 < inx_1 < inx_2


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if is_null(i, j, n):
            matrix[i][j] = 0

print_matrix(matrix, n, n, width=3)


#  Заполнение 5
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1

print_matrix(matrix, n, m, width=3)
