#  Все сразу 2
numbers = [8, 9, 10, 11]

numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)

print(numbers)


#  Переставить min и max

numbers = [int(i) for i in input().split()]

index_max = numbers.index(max(numbers))
index_min = numbers.index(min(numbers))
numbers[index_max], numbers[index_min] = numbers[index_min], numbers[index_max]

print(*numbers, sep=' ')


#  Количество артиклей
ARTICLES = ['a', 'an', 'the']

text = input().lower().split()

articles_count = 0
for el in ARTICLES:
    articles_count += text.count(el)

print(f'Общее количество артиклей: {articles_count}')


#  Взлом Братства Стали
n = input()
n = int(n[1:])

programme = []
for _ in range(n):
    line = input()
    if '#' in line:
        index_com = line.index('#')
        line = line[:index_com].rstrip()
    programme.append(line)

print(*programme, sep='\n')


#  Сортировка чисел
numbers = [int(i) for i in input().split()]

numbers.sort()
print(*numbers, sep=' ')
numbers.sort(reverse=True)
print(*numbers, sep=' ')
