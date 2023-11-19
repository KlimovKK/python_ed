#  Палиндром
word = input()

if word == word[::-1]:
    print('YES')
else:
    print('NO')


#  Делаем срезы 1
line = input()

print(len(line))
print(line * 3)
print(line[0])
print(line[:3])
print(line[-3:])
print(line[::-1])
print(line[1:len(line) - 1])


# Делаем срезы 2
line = input()

print(line[2])
print(line[-2])
print(line[:5])
print(line[:-2])
print(line[::2])
print(line[1::2])
print(line[::-1])
print(line[::-2])


#  Две половинки
line = input()

half_len = len(line) // 2 + len(line) % 2
print(line[half_len:] + line[:half_len])
