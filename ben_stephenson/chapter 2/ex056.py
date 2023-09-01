"""
Упражнение 56. Определение частоты
Электромагнитные волны можно классифицировать по частоте на семь
категорий, как показано в табл. 2.16.
Таблица 2.16. Частоты электромагнитных волн
Категория Диапазон частот (Гц)
Радиоволны Менее 3×109
Микроволны От 3×109 до 3×1012
Инфракрасное излучение От 3×1012 до 4,3×1014
Видимое излучение От 4,3×1014 до 7,5×1014
Ультрафиолетовое излучение От 7,5×1014 до 3×1017
Рентгеновское излучение От 3×1017 до 3×1019
Гамма-излучение Более 3×1019
Напишите программу, которая будет запрашивать у пользователя значе-
ние частоты волны и отображать название соответствующего излучения.
"""

wave_freq = float(input('Введите частоту волны (Гц): '))

if wave_freq < 3e9:
    category = 'радиоволны'
elif 3e9 <= wave_freq < 3e12:
    category = 'микроволны'
elif 3e12 <= wave_freq < 4.3e14:
    category = 'инфракрасное излучение'
elif 4.3e14 <= wave_freq < 7.5e14:
    category = 'видимое излучение'
elif 7.5e14 <= wave_freq < 3e17:
    category = 'ультрафиолетовое излучение'
elif 3e17 <= wave_freq < 3e19:
    category = 'рентгеновское излучение'
else:
    category = 'гамма-излучение'

print(f'Частоте {wave_freq} Гц соответствует {category}')