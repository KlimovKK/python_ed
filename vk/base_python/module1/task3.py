left, right = int(input()), int(input())
num = input()
flag = True

while num:
    if int(num) not in range(left, right + 1):
        flag = False
    num = input()

print(flag)
