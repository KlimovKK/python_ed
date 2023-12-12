#  Задача на программирование: небольшое число Фибоначчи
def fib(n):
    if n <= 1:
        return n
    else:
        fibonachi = [0, 1]
        for i in range(2, n + 1):
            fibonachi.append(fibonachi[i - 1] + fibonachi[i - 2])
        return fibonachi[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
