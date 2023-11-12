def average(line):
    line = [int(ch) for ch in line.split()]
    return round(sum(line) / len(line), 2)


line = input()
while line:
    print(average(line))
    line = input()
