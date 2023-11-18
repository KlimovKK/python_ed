def repeat_deco(n=1):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return my_decorator


# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
