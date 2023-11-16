def my_map(func, seq):
    for i in seq:
        yield func(i)


func_in, seq_in = eval(input()), eval(input())

for x in my_map(func_in, seq_in):
    print(x)
