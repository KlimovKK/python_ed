#  Наименьший делитель
n = int(input())

div = 1
for i in range(2, n + 1):
    if n % i == 0:
        div = i
        break

print(div)


#  Следуй правилам
n = int(input())

for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
