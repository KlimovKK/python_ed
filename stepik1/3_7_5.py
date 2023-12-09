"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно.
В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется
вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
В качестве ответа прикрепите файл с полученными данными о среднем росте.
"""
classes = {key: [] for key in range(1, 12)}
with open('dataset_3380_5.txt') as height:
    for line in height:
        line = line.strip().split()
        classes[int(line[0])].append(int(line[2]))

with open('result1.txt', 'w') as av_height:
    for key, value in classes.items():
        if value:
            value = sum(value) / len(value)
        else:
            value = '-'
        av_height.write(f'{key} {value}\n')