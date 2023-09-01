"""
Упражнение 52. Буквенные оценки – в числовые
В разных странах успеваемость студентов в университетах ведется по-
разному: где-то в качестве оценок используются буквы, где-то цифры.
Соответствие между ними приведено в табл. 2.13.
Таблица 2.13. Оценка успеваемости
Буквенная оценка Числовая оценка Буквенная оценка Числовая оценка
A+ 4,0 C+ 2,3
A 4,0 C 2,0
A- 3,7 C- 1,7
B+ 3,3 D+ 1,3
B 3,0 D 1,0
B- 2,7 F 0
Напишите программу, которая будет принимать на вход буквенную
оценку и выводить на экран соответствующую оценку в числовом выра-
жении. Убедитесь в том, что программа генерирует понятное сообщение
об ошибке при неверном вводе.
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

grade_let = input('Введите буквенную оценку: ').upper()

if grade_let == 'A+' or grade_let == 'A':
    grade_num = A
elif grade_let == 'A-':
    grade_num = A_MINUS
elif grade_let == 'B+':
    grade_num = B_PLUS
elif grade_let == 'B':
    grade_num = B
elif grade_let == 'B-':
    grade_num = B_MINUS
elif grade_let == 'C+':
    grade_num = C_PLUS
elif grade_let == 'C':
    grade_num = C
elif grade_let == 'C-':
    grade_num = C_MINUS
elif grade_let == 'D+':
    grade_num = D_PLUS
elif grade_let == 'D':
    grade_num = D
elif grade_let == 'F':
    grade_num = F
else:
    grade_num = FAIL

if grade_num == -1:
    print('Введите корректное обозначение оценки')
else:
    print(f'Буквенная {grade_let} оценка соотвествует {grade_num} баллам')
