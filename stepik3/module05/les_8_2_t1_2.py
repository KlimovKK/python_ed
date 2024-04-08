#  Тимур и его команда
n, m, k, x, y, z = [int(input()) for _ in range(6)]

all_students = n + m - x + k - y + z

print(all_students)


#  Книги на прочтение
n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

book_1_2 = n + m - x - t
book_2_3 = m + k - y - t
book_1_3 = n + k - z - t
book_1 = n - book_1_2 - book_1_3 - t
book_2 = m - book_1_2 - book_2_3 - t
book_3 = k - book_2_3 - book_1_3 - t
only_1 = book_1 + book_2 + book_3
only_2 = book_1_2 + book_1_3 + book_2_3
not_read = a - t - (book_1 + book_2 + book_3) - (book_1_2 + book_1_3 + book_2_3)

print(only_1, only_2, not_read, sep='\n')
