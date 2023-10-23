pas1, pas2 = input(), input()
if pas1 == pas2:
    print('Пароль принят')
else:
    print('Пароль не принят')

num = int(input())
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

num = int(input())
digit1 = num // 1000
digit2 = (num // 10 ** 2) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')

age = int(input())
if age < 18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')

