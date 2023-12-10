#  Максимальный в области 1
n = int(input())

el_in_area = []
for i in range(n):
    row = [int(num) for num in input().split()]
    el_in_area.extend(row[:i+1])

maximum = max(el_in_area)
print(maximum)


#  Максимальный в области 2
n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (j <= i <= n - j - 1 or j >= i >= n - j - 1) and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)


#  Суммы четвертей
def sum_quarter(expression, matrix, n):
    sm = 0
    for i in range(n):
        for j in range(n):
            if eval(expression):
                sm += matrix[i][j]
    return sm


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

answers = {'Верхняя четверть': 'i < j and i < n - 1 - j',
           'Правая четверть': 'i < j and i > n - 1 - j',
           'Нижняя четверть': 'i > j and i > n - 1 - j',
           'Левая четверть': 'i > j and i < n - 1 - j'}

for key, value in answers.items():
    print(f'{key}: {sum_quarter(value, matrix, n)}')
