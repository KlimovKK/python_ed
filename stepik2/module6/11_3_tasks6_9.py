#  Суммы двух
n = int(input())

res = []
first_num = int(input())
for _ in range(n - 1):
    second_num = int(input())
    res.append(first_num + second_num)
    first_num = second_num

print(res)
#  другое решение
seq = []
for _ in range(int(input())):
    seq.append(int(input()))

res = []
for i in range(len(seq) - 1):
    res.append(seq[i] + seq[i + 1])

print(res)


#  Удалите нечетные индексы
res = []
for _ in range(int(input())):
    res.append(int(input()))

del res[1::2]

print(res)


#  k-ая буква слова
n = int(input())

seq = []
for _ in range(n):
    seq.append(input())

res = ''
k = int(input())
for el in seq:
    res += el[k - 1: k]

print(res)


#  Символы всех строк
n = int(input())

res = []
for _ in range(n):
    line = input()
    res.extend(line)

print(res)
