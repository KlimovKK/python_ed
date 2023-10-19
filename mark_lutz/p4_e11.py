"""
Рекурсивные функции. Напишите простую рекурсивную функцию по имени countdown, которая выводит числа в ходе
обратного отсчета до нуля. Например, вызов countdown (5) должен вывести 5 4 3 2 1 stop. Нет очевидных причин
решать задачу с помощью явного стека или очереди, но как насчет подхода без использования функции?
Имеет ли смысл здесь применять генератор?
"""


def countdown(x):
    if x == 0:
        print('stop')
    else:
        print(x, end=' ')
        countdown(x - 1)


R = list(range(5, 0, -1))
print()
L = [print(i, end=' ') for i in range(5, 0, -1)]
print()
M = list(map(lambda x: print(x, end=' '), range(5, 0, -1)))
print()
countdown(5)


