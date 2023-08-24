"""
Упражнение 30. Цельсий в Фаренгейт и Кельвин
Напишите программу, которая будет запрашивать у пользователя значение
температуры в градусах Цельсия и отображать эквивалентный показатель
по шкалам Фаренгейта и Кельвина. Необходимые коэффициенты и фор-
мулы для проведения расчетов нетрудно найти на просторах интернета.
"""

t_c = float(input('Температура (°С): '))

t_f = (t_c * (9 / 5)) + 32
t_k = t_c + 273.15

print(f'Соответствует {t_f:.2f}°F и {t_k}K')