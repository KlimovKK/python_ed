def removes_duplicates(line):
    if len(line) <= 1:
        return line

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            line = line[:i] + line[i + 2:]
            break
    else:
        return line

    return removes_duplicates(line)


s = input()
print(removes_duplicates(s))
