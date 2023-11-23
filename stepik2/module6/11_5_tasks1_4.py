#  Построчный вывод
line = input().split()

print(*line, sep='\n')


#  Инициалы
name = input().split()

initials = '.'.join(word[0] for word in name) + '.'

print(initials)


#  Windows OS
path = input().split('\\')

print(*path, sep='\n')


#  Диаграмма
SYMBOL = '+'

list_of_numbers = input().split()

for num in list_of_numbers:
    print(SYMBOL * int(num))
