#  Цвет настроения синий
TEST = 'синий'
line = input()

if TEST in line:
    print('YES')
else:
    print('NO')


#  Отдыхаем ли?
DAY_1, DAY_2 = 'суббота', 'воскресенье'
line = input()

if DAY_1 in line or DAY_2 in line:
    print('YES')
else:
    print('NO')


#  Корректный email
TEST_1, TEST_2 = '@', '.'
email = input()

if TEST_1 in email and TEST_2 in email:
    print('YES')
else:
    print('NO')

