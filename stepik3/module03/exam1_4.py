# Каждый n-ый элемент
line = input().split()
n = int(input())

result_list = []
for i in range(n):
    tmp_list = []
    for j in range(i, len(line), n):
        tmp_list.append(line[j])
    result_list.append(tmp_list)

print(result_list)

# Максимальный в области 2
n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

largest = matrix[0][n - 1]

for i in range(n):
    for j in range(n):
        if i >= n - 1 - j and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)

# Транспонирование матрицы
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

matrix = [col for col in zip(*matrix)]

print_matrix(matrix, n, n)

# Снежинка
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = '*'
    matrix[i][n - i - 1] = '*'
    matrix[i][n // 2] = '*'
    matrix[n // 2][i] = '*'

print_matrix(matrix, n, n)
