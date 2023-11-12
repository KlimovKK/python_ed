line = input()

res = ''
counter = 0
for c in line:
    if c in '!%#@':
        counter += 1
    else:
        res += c.lower()

print(counter)
print(res)
