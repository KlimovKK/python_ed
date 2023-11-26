#  Найти всех
# объявление функции
def find_all(target, symbol):
    result = []
    for i, el in enumerate(target):
        if el == symbol:
            result.append(i)
    return result


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))


#  Merge lists 1
# объявление функции
def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))


#  Merge lists 2
def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]

    return result


n = int(input())

sort_numbers = [int(c) for c in input().split()]

for _ in range(n - 1):
    numbers = [int(c) for c in input().split()]
    sort_numbers = quick_merge(sort_numbers, numbers)

print(*sort_numbers, sep=' ')
