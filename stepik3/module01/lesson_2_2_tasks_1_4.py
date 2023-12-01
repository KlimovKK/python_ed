#  Координатные четверти
quarters = ['Первая', 'Вторая', 'Третья', 'Четвертая']

n = int(input())

cnt = [0, 0, 0, 0]
for _ in range(n):
    x, y = input().split()
    if int(y) > 0:
        if int(x) > 0:
            cnt[0] += 1
        elif int(x) < 0:
            cnt[1] += 1
    elif int(y) < 0:
        if int(x) < 0:
            cnt[2] += 1
        elif int(x) > 0:
            cnt[3] += 1

for i, el in enumerate(quarters):
    print(f'{el} четверть: {cnt[i]}')


#  Больше предыдущего
nums = [int(i) for i in input().split()]

count = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)


#  Назад, вперёд и наоборот
numbers = input().split()

for i in range(1, len(numbers), 2):
    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

print(*numbers)


#  Сдвиг в развитии
numbers = input().split()

numbers.insert(0, numbers.pop())

print(*numbers)
