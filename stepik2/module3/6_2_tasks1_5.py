print('"Python is a great language!", said Fred. ' + '"' + "I don't ever remember having this much fun before." + '"')


#  What's Your Name?
firstname = input()
lastname = input()

print('Hello', firstname, lastname + '! You have just delved into Python')


#  Футбольная команда
team = input()

print(f'Футбольная команда {team} имеет длину {len(team)} символов')


#  Три города
city_name_1, city_name_2, city_name_3 = input(), input(), input()

for name in (city_name_1, city_name_2, city_name_3):
    if len(name) == min(len(city_name_1), len(city_name_2), len(city_name_3)):
        short_name = name
    if len(name) == max(len(city_name_1), len(city_name_2), len(city_name_3)):
        long_name = name

print(short_name, long_name, sep='\n')


#  Арифметические строки
line_1, line_2, line_3 = input(), input(), input()

if (len(line_1) == (len(line_2) + len(line_3)) / 2 or len(line_2) == (len(line_1) + len(line_3)) / 2 or
        len(line_3) == (len(line_2) + len(line_1)) / 2):
    print('YES')
else:
    print('NO')
#  Решение  получше
len_1 = len(input())
len_2 = len(input())
len_3 = len(input())

if (2 * len_1 - len_2 - len_3) * (2 * len_2 - len_1 - len_3) * (2 * len_3 - len_1 - len_2) == 0:
    print('YES')
else:
    print('NO')
