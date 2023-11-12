line = input()

if ('a' in line or 'o' in line) and 'i' not in line and 'e' not in line:
    flag = True
else:
    flag = False

print(flag)
