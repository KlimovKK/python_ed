"""
Упражнение 69. Билеты в зоопарк
В зоопарке цена входного билета зависит от возраста посетителя. Дети до
двух лет допускаются бесплатно. Дети в возрасте от трех до 12 лет могут
посещать зоопарк за $14,00. Пенсионерам старше 65 лет вход обойдется
в $18,00, а обычный взрослый билет стоит $23,00.
Напишите программу, которая будет запрашивать возраст всех посети-
телей в группе (по одному за раз) и выводить общую цену билетов для по-
сещения зоопарка этой группой. В качестве индикатора окончания ввода
можно по традиции использовать пустую строку. Общую цену билетов
стоит выводить в формате с двумя знаками после запятой.
"""

#  Цены на билеты
CHILD_PRICE = 14.0
ADULT_PRICE = 23.0
AGED_PRICE = 18.0

age = input('Введите возраст первого посетителя: ')

#  Общая сумма
total = 0

while age != '':
    age = float(age)
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = CHILD_PRICE
    elif age >= 65:
        price = AGED_PRICE
    else:
        price = ADULT_PRICE