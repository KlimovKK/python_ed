import os

text = input()


def write_and_read(text):
    file_path = os.path.join(os.getcwd(), 'file_1')
    with open(file_path, 'w') as f:
        f.write(text)
    with open(file_path, 'r') as f:
        res = f.read().strip()

    return res


print(write_and_read(text))
