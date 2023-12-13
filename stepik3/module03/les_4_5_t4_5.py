#  Симметричная матрица
def is_symmetrical(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return 'NO'

    return 'YES'


n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

print(is_symmetrical(matrix, n))


#  Обмен диагоналей
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())

matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

print_matrix(matrix, n, n)
