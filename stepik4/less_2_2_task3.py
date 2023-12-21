def fib_mod(n, m):
    piz = [0, 1]
    for num in range(2, 6 * m + 2):
        piz.append((piz[-2] + piz[-1]) % m)
        if piz[-2] == 0 and piz[-1] == 1:
            break

    return piz[n % (num - 1)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
