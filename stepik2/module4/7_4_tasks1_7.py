#  До КОНЦА 1
END = 'КОНЕЦ'

text = input()
while text != END:
    print(text)
    text = input()


#  До КОНЦА 2
END = ('КОНЕЦ', 'конец')

text = input()
while text not in END:
    print(text)
    text = input()


#  Количество членов
END = ('стоп', 'хватит', 'достаточно')

text = input()
counter = 0
while text not in END:
    counter += 1
    text = input()

print(counter)


#  Пока делимся
DIVISOR = 7

num = int(input())

while num % DIVISOR == 0:
    print(num)
    num = int(input())


#  Сумма чисел
num = int(input())

total = 0
while num >= 0:
    total += num
    num = int(input())

print(total)


#  Количество пятерок
grade = int(input())

count_5 = 0
while 0 <= grade <= 5:
    if grade == 5:
        count_5 += 1
    grade = int(input())

print(count_5)


#  Ведьмаку заплатите чеканной монетой
MINTED_COIN_1 = 1
MINTED_COIN_5 = 5
MINTED_COIN_10 = 10
MINTED_COIN_25 = 25

witcher_price = int(input())

count_coins = 0
while witcher_price:
    for i in (MINTED_COIN_25, MINTED_COIN_10, MINTED_COIN_5, MINTED_COIN_1):
        coins = witcher_price // i
        if coins > 0:
            count_coins += coins
            witcher_price -= coins * i

print(count_coins)
