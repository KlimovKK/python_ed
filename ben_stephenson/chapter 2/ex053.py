"""
Упражнение 53. Числовые оценки – в буквенные
В предыдущем упражнении мы переводили буквенные оценки студен-
тов в числовые. Сейчас перевернем ситуацию и попробуем определить
буквенный номинал оценки по его числовому эквиваленту. Убедитесь
в том, что ваша программа будет обрабатывать числовые значения между
указанными в табл. 2.13. В этом случае оценки должны быть округлены до
ближайшей буквы. Программа должна выдавать оценку A+, если введен-
ное пользователем значение будет 4,0 и выше.
"""
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
FAIL = -1

grade_num = float(input('Введите числовое обозначение оценки: '))

if grade_num >= A:
    grade_let = 'A+'
elif A > grade_num >= (A - A_MINUS) / 2 + A_MINUS:
    grade_let = 'A'
elif (A - A_MINUS) / 2 + A_MINUS > grade_num >= (A_MINUS - B_PLUS) / 2 + B_PLUS:
    grade_let = 'A-'
elif (A_MINUS - B_PLUS) / 2 + B_PLUS > grade_num >= (B_PLUS - B) / 2 + B:
    grade_let = 'B+'
elif (B_PLUS - B) / 2 + B > grade_num >= (B - B_MINUS) / 2 + B_MINUS:
    grade_let = 'B'
elif (B - B_MINUS) / 2 + B_MINUS > grade_num >= (B_MINUS - C_PLUS) / 2 + C_PLUS:
    grade_let = 'B-'
elif (B_MINUS - C_PLUS) / 2 + C_PLUS > grade_num >= (C_PLUS - C) / 2 + C:
    grade_let = 'C+'
elif (C_PLUS - C) / 2 + C > grade_num >= (C - C_MINUS) / 2 + C_MINUS:
    grade_let = 'C'
elif (C - C_MINUS) / 2 + C_MINUS > grade_num >= (C_MINUS - D_PLUS) / 2 + D_PLUS:
    grade_let = 'C-'
elif (C_MINUS - D_PLUS) / 2 + D_PLUS > grade_num >= (D_PLUS - D) / 2 + D:
    grade_let = 'D+'
elif (D_PLUS - D) / 2 + D > grade_num >= D / 2:
    grade_let = 'D'
elif D / 2 > grade_num >= F:
    grade_let = 'F'
else:
    grade_let = ''

if grade_let == '':
    print('Числовой эквивалент оценки должен быть больше 0')
else:
    print(f'{grade_num} баллам соответствует буквенная оценка {grade_let}')
