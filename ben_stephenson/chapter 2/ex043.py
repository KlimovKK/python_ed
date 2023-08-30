"""
Упражнение 43. Узнать ноту по частоте
В предыдущем упражнении мы определяли частоту ноты по ее назва-
нию и номеру октавы. Теперь выполним обратную операцию. Запроси-
те у пользователя частоту звука. Если введенное значение укладывается
в диапазон ±1 Гц от значения в таблице, выведите на экран название
соответствующей ноты. В противном случае сообщите пользователю,
что ноты, соответствующей введенной частоте, не существует. В данном
упражнении можно ограничиться только нотами, приведенными в табли-
це. Нет необходимости брать в расчет другие октавы.
"""

C4_freq = 261.63
D4_freq = 293.63
E4_freq = 329.63
F4_freq = 349.23
G4_freq = 392.00
A4_freq = 440.00
B4_freq = 493.88
diapason = 1

freq = float(input('Введите частоту (Гц): '))

if C4_freq - diapason <= freq <= C4_freq + diapason:
    note = 'C4'
elif D4_freq - diapason <= freq <= D4_freq + diapason:
    note = 'D4'
elif E4_freq - diapason <= freq <= E4_freq + diapason:
    note = 'E4'
elif F4_freq - diapason <= freq <= F4_freq + diapason:
    note = 'F4'
elif G4_freq - diapason <= freq <= G4_freq + diapason:
    note = 'G4'
elif A4_freq - diapason <= freq <= A4_freq + diapason:
    note = 'A4'
elif B4_freq - diapason <= freq <= B4_freq + diapason:
    note = 'B4'
else:
    note = ''

if note == '':
    print(f'В четвертой октаве нет ноты с частотой {freq} Гц')
else:
    print(f'Частоте {freq} соответствует нота {note}')
