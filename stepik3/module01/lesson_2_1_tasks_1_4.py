#  На easy
a, b = int(input()), int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** .5)


#  Индекс массы тела
weight, height = float(input()), float(input())

BMI = weight / height ** 2
if BMI > 25:
    res = 'Избыточная масса'
elif BMI < 18.5:
    res = 'Недостаточная масса'
else:
    res = 'Оптимальная масса'

print(res)


#  Стоимость строки
SYMBOL_COST = .60

text = input()
line_cost = len(text) * SYMBOL_COST
rub = int(line_cost // 1)
kop = round(line_cost % 1 * 100)

print(f'{rub} р. {kop} коп.')


#  Количество слов
print(len(input().split()))
