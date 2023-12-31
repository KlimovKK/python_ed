"""
Итерации и включения. Напишите код для построения нового списка, содержащего квадратные корни всех чисел
из следующего списка: [2, 4, 9, 16, 25]. Сначала запишите его как цикл for, затем как вызов map,
далее как списковое включение и наконец как генераторное выражение. Для вычисления квадратного корня применяйте
функцию sqrt из встроенного модуля math (например, импортируйте math и вызовите math.sqrt(х)).
Какой из четырех подходов вам представляется наилучшим?
"""
from math import sqrt
L = [2, 4, 9, 16, 25]
new = []
for c in L:
    new.append(sqrt(c))
print(new)

new = list(map(sqrt, L))
print(new)

new = [sqrt(x) for x in L]
print(new)

new = list(sqrt(x) for x in L)
print(new)