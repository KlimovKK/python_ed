#  Заполнение спиралью
def fills_in_matrix(num, row_start, row_end, col_start, col_end, step=1):
    fills_in_matrix.counter += 1
    for i in range(row_start, row_end, step):
        for j in range(col_start, col_end, step):
            matrix[i][j] = num
            num += 1
    return num


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = (int(i) for i in input().split())
matrix = [[0] * m for _ in range(n)]
fills_in_matrix.counter = 0

num = 1
while num <= n * m:
    direction = fills_in_matrix.counter % 4
    k = fills_in_matrix.counter // 4
    if direction == 0:
        num = fills_in_matrix(num, k, k + 1, k, m - k)
    elif direction == 1:
        num = fills_in_matrix(num, k + 1, n - k, m - 1 - k, m - k)
    elif direction == 2:
        num = fills_in_matrix(num, n - 1 - k, n - 2 - k, m - 2 - k, -1 + k, step=-1)
    else:
        num = fills_in_matrix(num, n - 2 - k, k, k, k - 1, step=-1)

print_matrix(matrix, n, m, width=3)
