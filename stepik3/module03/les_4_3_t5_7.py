#  Упаковка дубликатов
line = input().split()

duplicates = [list(line[:1])]
for c in line[1:]:
    cur_el = duplicates[len(duplicates) - 1]
    if c in cur_el:
        cur_el.append(c)
    else:
        duplicates.append(list(c))

print(duplicates)
#  Другое решение (совсем забыл про отрицательные индексы)
s = input().split()
# кидаем первый символ в наш список, также удалив его из входного списка
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)


#  Разбиение на чанки
def chunked(lst, num):
    result = []
    while lst:
        result.append(lst[:num])
        lst[:num] = []
    return result


line = input().split()
n = int(input())

print(chunked(line, n))


#  Подсписки списка
line = input().split()

sublists = [[]]
for step in range(1, len(line) + 1):
    for i in range(len(line) + 1 - step):
        sublists.append(list(line[i:i + step]))

print(sublists)
