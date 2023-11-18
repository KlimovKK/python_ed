def cache_deco(func):
    def wrapper(*args, **kwargs):
        if args in my_dict:
            return my_dict[args]
        else:
            result = func(*args, **kwargs)
            my_dict[args] = result
            return result

    return wrapper


def solution(func_map, func_filter, data):
    for i, el in enumerate(map(func_map, filter(func_filter, data))):
        if i % 2 == 0:
            yield el


my_dict = {}

# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
