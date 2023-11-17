#  12 месяцев
total = 0
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            nkm = n * 28 + k * 30 + m * 31
            if n * 28 + k * 30 + m * 31 == 365:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)


#  Старинная задача
for b in range(101):
    for c in range(101):
        for t in range(101):
            if 10 * b + 5 * c + 0.5 * t == 100 and b + c + t == 100:
                print(f'быков {b}, коров {c}, телят {t}')


#  Гипотеза Эйлера о сумме степеней
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum1 = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(sum1 ** (1/5))
                if sum1 == e ** 5:
                    print(a, b, c, d, e, 'sum=', a+b+c+d+e)
                    break
