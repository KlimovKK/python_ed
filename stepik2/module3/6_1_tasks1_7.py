#  Площадь треугольника
a, b = float(input()), float(input())

S = (a * b) / 2
print(S)


#  Две старушки (скорость сближения)
s, v1, v2 = float(input()), float(input()), float(input())

t = s / (v1 + v2)
print(t)


#  Обратное число
num = float(input())

if num != 0:
    res = 1 / num
else:
    res = 'Обратного числа не существует'
print(res)


#  451 градус по Фаренгейту
F = float(input())

C = 5 / 9 * (F - 32)
print(C)


#  Dog age
n = int(input())

if n <= 2:
    hum_age = n * 10.5
else:
    hum_age = (n - 2) * 4 + 21
print(hum_age)


#  Первая цифра после точки
num = float(input())

res = int(num * 10) % 10
print(res)


#  Дробная часть
num = float(input())

res = num - int(num)
print(res)
