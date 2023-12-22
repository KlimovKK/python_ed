def sorts_grades(grades_list, size):
    for i in range(size - 1, -1, -1):
        if grades_list[i] == 0:
            grades_list.append(grades_list.pop(i))


size = int(input())
grades = [int(num) for num in input().split()]

sorts_grades(grades, size)
print(*grades)
