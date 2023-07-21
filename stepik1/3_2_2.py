"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов
и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы,
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода
и выводить для каждого уникального слова в этой строке число его
повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное
слово должно выводиться только один раз.
"""
warandheace = [i for i in input().lower().split()]
d = {}
for word in warandheace:
    amount = warandheace.count(word)
    if word not in d:
        d[word] = amount

for word, amount in d.items():
    print(word, amount)
