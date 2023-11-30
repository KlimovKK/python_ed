#  Зодиак
ANIMALS = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык',
           'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']

year = int(input())

animal = ANIMALS[year % 12]

print(animal)


#  Переворот числа
num = input()

res = int(num[:-5] + num[:-6:-1])

print(res)


#  Standard American Convention
n = int(input())

print(f'{n:,}')


#  Задача Иосифа Флавия
n, k = int(input()), int(input())

people = list(range(1, n + 1))
while len(people) > 1:
    for i in range(k - 1):
        temp = people.pop(0)
        people.append(temp)
    del people[0]

print(people[0])
