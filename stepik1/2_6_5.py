"""
Выведите таблицу размером n*n, заполненную числами от 1 до n^2 по спирали, выходящей из
левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""
n = int(input())
tbl = [[0 for j in range(n)] for i in range(n)]
if n % 2 == 0:
    c =1
else:
    c = 0
s = 1
bj, bi = n, n
ej, ei = 0, 0
i, j = 0, 0
while s != n**2 + c:
    for napr in range(4):
        if napr == 0:
            for j in range(n - bj, n - ej):
                tbl[i][j] = s
                s += 1
            bi -= 1
        elif napr == 1:
            for i in range(n - bi, n - ei):
                tbl[i][j] = s
                s += 1
            ej += 1
        elif napr == 2:
            for j in range(n - ej - 1, n - bj - 1, -1):
                tbl[i][j] = s
                s += 1
            ei += 1
        else:
            for i in range(n - ei - 1, n - bi - 1, -1):
                tbl[i][j] = s
                s += 1
            bj -= 1
if n == 1:
    tbl[i][j] = s
elif c == 0:
    tbl[i][j + 1] = s
for i in range(n):
    print(*[tbl[i][j] for j in range(n)])