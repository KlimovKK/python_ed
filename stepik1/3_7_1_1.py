# Не моё
a = [input().split(';') for i in range(int(input()))]
b = {i: [] for i in set([i[0] for i in a]) | set([i[2] for i in a])}
for i in a:
    b[i[0]].append(1 if i[1] == i[3] else 3 if i[1] > i[3] else 0)
    b[i[2]].append(1 if i[1] == i[3] else 3 if i[1] < i[3] else 0)
for i in b: print('%s:%i %i %i %i %i' % (i, len(b[i]), b[i].count(3), b[i].count(1), b[i].count(0), sum(b[i])))
