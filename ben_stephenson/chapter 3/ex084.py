"""
Упражнение 84. Подбрасываем монетку
Какое минимальное количество раз вы должны подбросить монетку, что-
бы три раза подряд выпал либо орел, либо решка? А какое максимальное
количество попыток может для этого понадобиться? А в среднем? В дан-
ном упражнении мы выясним это, создав симулятор подбрасывания вир-
туальной монетки.
Напишите программу, использующую для подброса монетки генера-
тор случайных чисел Python. Монетка при этом должна быть правильной
формы, что означает равную вероятность выпадения орла и решки. Под-
брасывать монетку необходимо до тех пор, пока три раза подряд не вы-
падет одно значение, вне зависимости от того, орел это будет или решка.
Выводите на экран букву О всякий раз, когда выпадает орел, и Р – когда
выпадает решка. При этом для одной симуляции бросков все выпавшие
значения необходимо размещать на одной строке. Также необходимо из-
вестить пользователя о том, сколько попыток потребовалось, чтобы полу-
чить нужный результат.
Программа должна выполнить десять симуляций и в конце представить
среднее количество подбрасываний монетки, требуемое для достижения
нужного нам результата. Пример вывода программы показан ниже:
О Р Р Р (попыток: 4)
О О Р Р О Р О Р Р О О Р О Р Р О Р Р Р (попыток: 19)
Р Р Р (попыток: 3)
Р О О О (попыток: 4)
О О О (попыток: 3)
Р О Р Р О Р О О Р Р О О Р О Р О О О (попыток: 18)
О Р Р О О О (попыток: 6)
Р О Р Р Р (попыток: 5)
Р Р О Р Р О Р О Р О О О (попыток: 12)
Р О Р Р Р (попыток: 5)
Среднее количество попыток: 7,9.
"""

from random import randrange

NUM_SIM = 10  # Количество симуляций
NUM_REP = 3  # Количество повторов для прекращения

sum_attemps = 0

for i in range(NUM_SIM):
    throw = randrange(0, 2)  # Бросок монетки
    qty_rep = 1  # Количество повторов
    attemps = 1  # Количество попыток в каждой итерации
    print(f'{"О" if throw == 0 else "Р"}', end=' ')
    while qty_rep < NUM_REP:
        prev_throw = throw  # Запоминаем предыдущий бросок
        throw = randrange(0, 2)
        if throw == prev_throw:
            qty_rep += 1
            print(f'{"О" if throw == 0 else "Р"}', end=' ')
        else:
            qty_rep = 1
            print(f'{"О" if throw == 0 else "Р"}', end=' ')
        attemps += 1
    print(f'(попыток: {attemps})')
    sum_attemps += attemps

print(f'Среднее количество попыток: {sum_attemps / NUM_SIM:.2f}')