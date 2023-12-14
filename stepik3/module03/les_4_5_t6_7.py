#  Зеркальное отображение
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

print_matrix(matrix, n, n)


#  Поворот матрицы
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

matrix = [list(reversed(col)) for col in zip(*matrix)]

print_matrix(matrix, n, n)
