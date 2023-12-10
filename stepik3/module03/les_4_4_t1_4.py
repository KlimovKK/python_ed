#  Вывести матрицу 1
def print_matrix(mtx, n, m):
    for r in range(n):
        for c in range(m):
            print(mtx[r][c], end=' ')
        print()


n, m = int(input()), int(input())
matrix = [[input() for j in range(m)] for i in range(n)]

print_matrix(matrix, n, m)
#  Короткое решение
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)


#  Вывести матрицу 2
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)
print()
for c in range(m):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()


#  След матрицы
n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

total = 0
for i in range(n):
    total += matrix[i][i]

print(total)


#  Больше среднего
n = int(input())
counts = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    average_cnt = [i for i in row if i > sum(row) / len(row)]
    counts.append(len(average_cnt))

print(*counts, sep='\n')
