def fib_digit(n):
    digit = 1
    a, b = 0, 1
    for num in range(2, n + 1):
        digit = (a + b) % 10
        a, b = b, digit

    return digit


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
