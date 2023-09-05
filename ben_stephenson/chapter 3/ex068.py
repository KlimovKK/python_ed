"""
Упражнение 68. Средняя оценка
В задаче 52 мы уже создавали таблицу соответствий между оценками
в буквенном и числовом выражении. Сейчас вам нужно будет рассчитать
среднюю оценку по произвольному количеству введенных пользователем
буквенных оценок. Для окончания ввода можно использовать индикатор
в виде пустой строки. Например, если пользователь последовательно вве-
дет оценки A, затем C+, а после этого B и пустую строку, средний результат
должен составить 3,1.
Для расчетов вам может пригодиться математика из упражнения 52.
Никаких проверок на ошибки проводить не нужно. Предположим, что
пользователь может вводить только корректные оценки или ноль.
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

grade_let = input('Введите буквенную оценку (пустое поля для завершения): ').upper()
qty = 0         # Количество оценок
sum_grades = 0  # Сумма оценок

while grade_let != '':
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
    else:
        grade_num = F

    sum_grades += grade_num
    qty += 1
    grade_let = input('Введите буквенную оценку (пустое поля для завершения): ').upper()

average = sum_grades / qty
print(f'Средняя оценка составляет {average:.1f} баллов')
