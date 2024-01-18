def is_anagram(a, b):
    if len(a) != len(b):
        return 'false'

    hash_a = {}
    hash_b = {}
    for ch in a:
        if ch in hash_a:
            hash_a[ch] += 1
        else:
            hash_a[ch] = 1
    for ch in b:
        if ch in hash_b:
            hash_b[ch] += 1
        else:
            hash_b[ch] = 1

    if hash_a == hash_b:
        return 'true'

    return 'false'


def reads_line(line):
    line = line.split()
    a = ''.join([ch for ch in line[0] if ch.isalpha()])
    b = ''.join([ch for ch in line[1] if ch.isalpha()])
    return a, b


a, b = reads_line(input())
print(is_anagram(a, b))
