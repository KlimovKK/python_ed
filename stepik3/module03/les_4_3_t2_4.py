#  Список по образцу 2
n = int(input())

res = []
for i in range(1, n + 1):
    res.append([j for j in range(1, i + 1)])

print(*res, sep='\n')


#  Треугольник Паскаля 1
from math import factorial


def pascal(n):
    result = []
    for m in range(n + 1):
        el = int(factorial(n) / (factorial(m) * factorial(n - m)))
        result.append(el)

    return result


n = int(input())

print(pascal(n))
#  Другое решение
def pascal(n):
    # начальная строка
    cur_seq = [1]

    for _ in range(n):
        # добавляем нули по бокам к текущей строке строке
        cur_seq = [0] + cur_seq + [0]
        # тут будет храниться новая строка
        new_seq = []

        for i in range(len(cur_seq) - 1):
            # добавляем в новую строку сумму соседних элементов текущей строки
            new_seq.append(cur_seq[i] + cur_seq[i + 1])

        # теперь новая строка становится нашей текущей строкой
        cur_seq = new_seq

    return cur_seq


n = int(input())
print(pascal(n))


#  Треугольник Паскаля 2
from math import factorial


def pascal(n):
    result = []
    for m in range(n + 1):
        el = int(factorial(n) / (factorial(m) * factorial(n - m)))
        result.append(el)

    return result


n = int(input())

for i in range(n):
    print(*pascal(i))
