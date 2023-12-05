#  Камень, ножницы, бумага, ящерица, Спок
SHAPES = ['ножницы', 'бумага', 'камень', 'ящерица', 'спок']
choice_1, choice_2 = input().lower(), input().lower()

diff = SHAPES.index(choice_1) - SHAPES.index(choice_2)
if choice_1 == choice_2:
    res = 'ничья'
elif diff in [-3, -1, 2, 4]:
    res = 'Тимур'
else:
    res = 'Руслан'

print(res)

#  Другое решение
options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)


#  Орел и решка
line = input().split('О')

res = max(map(len, line))

print(res)
