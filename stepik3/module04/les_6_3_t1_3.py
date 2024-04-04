#  Вершина параболы
a, b, c = [int(input()) for _ in range(3)]

coord = (-b / (2 * a), (4 * a * c - b ** 2) / (4 * a))

print(coord)


#  Конкурсный отбор
def print_list(schoolkids, min_grade):
    for schoolkid in schoolkids:
        if schoolkid[1] >= min_grade:
            print(*schoolkid)


n = int(input())
class_list = [tuple(int(i) if i.isdigit() else i for i in input().split()) for _ in range(n)]

print_list(class_list, 1)
print()
print_list(class_list, 4)


#  Последовательность Трибоначчи
n = int(input())
t1, t2, t3 = 1, 1, 1
for i in range(n):
    print(t1, end=' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3
