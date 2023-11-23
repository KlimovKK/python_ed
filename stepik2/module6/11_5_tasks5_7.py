#  Корректный ip-адрес
ip = input().split('.')

flag = 'ДА'
for el in ip:
    if int(el) < 0 or int(el) > 255:
        flag = 'НЕТ'
        break

print(flag)


#  Добавь разделитель
text = input()
delimiter = input()

print(delimiter.join(text))


#  Количество совпадающих пар
list_of_numbers = input().split()

count_pairs = 0
for i in range(len(list_of_numbers) - 1):
    for j in range(i + 1, len(list_of_numbers)):
        if list_of_numbers[i] == list_of_numbers[j]:
            count_pairs += 1

print(count_pairs)
