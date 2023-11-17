def cache_deco(func):
    def wrapper(*args, **kwargs):
        if args in my_dict:
            return my_dict[args]
        else:
            result = func(*args, **kwargs)
            my_dict[args] = result
            return result

    return wrapper


my_dict = {}
code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
