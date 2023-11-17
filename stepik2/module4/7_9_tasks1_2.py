#  Численный треугольник 2
n = int(input())

total = 1
for i in range(n):
    for j in range(i + 1):
        print(total, end=' ')
        total += 1
    print()


#  Численный треугольник 3
n = int(input())

for i in range(n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, - 1):
        print(j, end='')
    print()
