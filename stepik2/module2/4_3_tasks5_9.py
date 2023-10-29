#  Вес боксера
wt = int(input())

if wt < 60:
    category = 'Легкий вес'
elif wt < 64:
    category = 'Первый полусредний вес'
elif wt < 69:
    category = 'Полусредний вес'
print(category)


#  Калькулятор
num1, num2 = int(input()), int(input())
operation = input()

if operation == '+':
    res = num1 + num2
elif operation == '-':
    res = num1 - num2
elif operation == '*':
    res = num1 * num2
elif operation == '/':
    if num2 != 0:
        res = num1 / num2
    else:
        res = 'На ноль делить нельзя!'
else:
    res = 'Неверная операция'
print(res)


#  Цветовой микшер
RED = 'красный'
BLUE = 'синий'
YELLOW = 'желтый'
VIOLET = 'фиолетовый'
ORANGE = 'оранжевый'
GREEN = 'зеленый'
color1, color2 = input(), input()

if (color1 == RED or color1 == BLUE or color1 == YELLOW) and (color2 == RED or color2 == BLUE or color2 == YELLOW):
    if color1 == color2:
        mix_color = color1
    elif (color1 == RED or color1 == BLUE) and (color2 == BLUE or color2 == RED):
        mix_color = VIOLET
    elif (color1 == RED or color1 == YELLOW) and (color2 == YELLOW or color2 == RED):
        mix_color = ORANGE
    else:
        mix_color = GREEN
else:
    mix_color = 'ошибка цвета'

print(mix_color)


#  Цвет карманов колеса рулетки
num = int(input())

if 0 <= num <= 36:
    if num == 0:
        color = 'зеленый'
    elif num % 2 == 0 and (num <= 10 or 19 <= num <= 28):
        color = 'черный'
    elif num % 2 == 1 and (11 <= num <= 18 or num >= 29):
        color = 'черный'
    else:
        color = 'красный'
else:
    color = 'ошибка ввода'

print(color)


#  Пересечение отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 > a2:
    a1, a2 = a2, a1
    b1, b2 = b2, b1
if b1 < a2:
    res = 'пустое множество'
elif b1 == a2:
    res = str(b1)
else:
    if b2 < b1:
        b1 = b2
    res = str(a2) + ' ' + str(b1)

print(res)
