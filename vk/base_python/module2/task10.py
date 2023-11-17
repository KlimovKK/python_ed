def f():
    b = int(input())

    def g():
        nonlocal b
        b += 10

    g()
    print(b)


f()
