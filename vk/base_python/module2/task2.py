DEL_CHAR = '!@#%'

def transform(line):
    if line[0] == '!':
        res = ''.join(ch for ch in line if ch not in DEL_CHAR).upper()
    else:
        res = ''.join(ch for ch in line if ch not in DEL_CHAR).lower()
    return res


line = input()
while line:
    print(transform(line))
    line = input()
