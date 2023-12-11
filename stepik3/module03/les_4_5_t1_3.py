#  Таблица умножения
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = int(input()), int(input())

mult = [[i * j for j in range(m)] for i in range(n)]

print_matrix(mult, n, m, 3)


#  Максимум в таблице
n, m = int(input()), int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

max_index = (0, 0)
for i in range(n):
    for j in range(m):
        if matrix[max_index[0]][max_index[1]] < matrix[i][j]:
            max_index = (i, j)

print(*max_index)


#  Обмен столбцов
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = int(input()), int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]
i, j = (int(k) for k in input().split())

for row in matrix:
    row[i], row[j] = row[j], row[i]

print_matrix(matrix, n, m)
