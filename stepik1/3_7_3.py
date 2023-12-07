"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество d известных нам слов,
после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
"""


def dictionary_search(text):
    result = set()
    for word in text.split():
        if word not in words:
            result.add(word)

    return result


d = int(input())
words = [input().lower() for _ in range(d)]
l = int(input())

res = set()
for _ in range(l):
    line = input().lower()
    res.update(dictionary_search(line))

print(*res, sep='\n')
