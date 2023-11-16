def fibonacci(x):
    if x in fibo_dict:
        return fibo_dict[x]
    else:
        fibo_dict[x] = fibonacci(x - 1) + fibonacci(x - 2)
        return fibonacci(x - 1) + fibonacci(x - 2)


n = int(input())

fibo_dict = {1: 1, 2: 1}
print(fibonacci(n))
