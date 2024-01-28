# Симметричная матрица
def is_symmetrical(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                return 'NO'

    return 'YES'


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

print(is_symmetrical(matrix, n))

# Латинский квадрат
def is_latin_square(matrix, n):
    example = set(range(1, n + 1))
    for i in range(n):
        row = []
        col = []
        for j in range(n):
            row.append(matrix[i][j])
            col.append(matrix[j][i])
        if set(row) != example or set(col) != example:
            return 'NO'

    return 'YES'


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
print(is_latin_square(matrix, n))

# Ходы ферзя
CHESS_COL = 'abcdefgh'


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


queen_square = input()
chess_board = [['.'] * 8 for _ in range(8)]
queen_square = [abs(int(queen_square[1]) - 8), CHESS_COL.index(queen_square[0])]

for i in range(8):
    for j in range(8):
        if abs(queen_square[0] - i) == abs(queen_square[1] - j) or queen_square[0] == i or queen_square[1] == j:
            chess_board[i][j] = '*'

chess_board[queen_square[0]][queen_square[1]] = 'Q'

print_matrix(chess_board, 8, 8)

# Диагонали, параллельные главной
def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[abs(i - j) for j in range(n)] for i in range(n)]

print_matrix(matrix, n, n)
