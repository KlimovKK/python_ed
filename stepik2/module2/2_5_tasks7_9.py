num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)

num = int(input())
c = num % 10
b = (num // 10) % 10
a = num // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

num = int(input())
d4 = num % 10
d3 = (num // 10) % 10
d2 = (num // 10 ** 2) % 10
d1 = (num // 10 ** 3) % 10
print('Цифра в позиции тысяч равна', d1)
print('Цифра в позиции сотен равна', d2)
print('Цифра в позиции десятков равна', d3)
print('Цифра в позиции единиц равна', d4)
