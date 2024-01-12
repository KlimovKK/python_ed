def sort_books(books_list, n):
    result = merge_sort(books_list, 2)
    one_year = []
    i = 0
    while i < n - 1:
        one_year.append(result[i])
        start = i
        while result[i][2] == result[i + 1][2]:
            one_year.append(result[i + 1])
            i += 1
        temp = merge_sort(one_year, 1)
        result[start:i + 1] = temp
        i += 1
        one_year = []
    return result


def merge_sort(array, idx):
    if len(array) <= 1:
        return array

    mid_index = len(array) // 2
    left = array[:mid_index]
    right = array[mid_index:]

    left = merge_sort(left, idx)
    right = merge_sort(right, idx)

    return merge(left, right, idx)


def merge(left, right, idx):
    merged_arr = []
    l_index, r_index = 0, 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index][idx] < right[r_index][idx]:
            merged_arr.append(left[l_index])
            l_index += 1
        else:
            merged_arr.append(right[r_index])
            r_index += 1
    while l_index < len(left):
        merged_arr.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        merged_arr.append(right[r_index])
        r_index += 1

    return merged_arr


def reads_list(n):
    books = []
    for _ in range(n):
        isdn, title, year = input().split('"')
        books.append((isdn.strip(), '"' + title + '"', int(year)))

    return books


def prints_list(books):
    for book in books:
        print(*book)


n = int(input())
books_list = reads_list(n)
sorted_books_list = sort_books(books_list, n)
prints_list(sorted_books_list)
