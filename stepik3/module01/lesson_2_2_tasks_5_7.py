#  Различные элементы
numbers = input().split()

res = []
for el in numbers:
    if el not in res:
        res.append(el)

print(len(res))


#  Произведение чисел
def check_product(list_nums, test):
    for i in list_nums:
        for j in list_nums[list_nums.index(i) + 1:]:
            if i * j == test:
                return 'ДА'

    return 'НЕТ'


n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
product = int(input())

print(check_product(numbers, product))


#  Камень, ножницы, бумага
SHAPES = ['камень', 'ножницы', 'бумага']
choice_1, choice_2 = input().lower(), input().lower()

diff = SHAPES.index(choice_1) - SHAPES.index(choice_2)
if choice_1 == choice_2:
    res = 'ничья'
elif diff in [-1, 2]:
    res = 'Тимур'
else:
    res = 'Руслан'

print(res)
# Лучший вариант
options = ["камень", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)
