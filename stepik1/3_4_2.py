"""
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.
"""

with open('dataset_3363_3.txt') as inf:
    text = inf.read().lower().strip().split()

maxc = 0
text.sort()
for word in text:
    amount = text.count(word)
    if amount > maxc:
        maxc = amount
        freq_word = word

print(freq_word + ' ' + str(maxc))