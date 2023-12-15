#  Заполнение змейкой
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = m * i + ((i + 1) % 2) * (j + 1) + (i % 2) * (m - j)

print_matrix(matrix, n, m, width=3)


#  Заполнение диагоналями
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix = [[0] * m for _ in range(n)]

next_num = 0
for k in range(n + m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                next_num += 1
                matrix[i][j] = next_num

print_matrix(matrix, n, m, width=3)
