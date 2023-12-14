#  Ходы коня
CHESS_COL = 'abcdefgh'


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


knights_square = input()
chess_board = [['.'] * 8 for _ in range(8)]
knights_square = [abs(int(knights_square[1]) - 8), CHESS_COL.index(knights_square[0])]

for i in range(8):
    for j in range(8):
        knights_move = (knights_square[0] - i) * (knights_square[1] - j)
        if knights_move in [-2, 2]:
            chess_board[i][j] = '*'

chess_board[knights_square[0]][knights_square[1]] = 'N'

print_matrix(chess_board, 8, 8)


#  Магический квадрат
def is_all_numbers(numbers, matrix):
    nums_in_matrix = [j for i in matrix for j in i]
    return set(nums_in_matrix) == set(numbers)


def is_magic(matrix, num):
    first = sum(matrix[0])
    sum_principal_diag = 0
    sum_secondary_diag = 0
    for i in range(1, num):
        if sum(matrix[i]) != first:
            return False
    for i in range(num):
        if sum([row[i] for row in matrix]) != first:
            return False
        sum_principal_diag += matrix[i][i]
        sum_secondary_diag += matrix[i][num - i - 1]

    return first == sum_principal_diag == sum_secondary_diag


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
numbers = list(range(1, n ** 2 + 1))

if is_all_numbers(numbers, matrix) and is_magic(matrix, n):
    print('YES')
else:
    print('NO')
