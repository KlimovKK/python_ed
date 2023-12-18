#  Добавлена папка /tmp
import os

text = input()


def write_and_read(text):
    file_path = os.path.join(os.path.abspath('/tmp'), 'file_1')
    open(file_path, 'w').write(text)
    return open(file_path).read()


print(write_and_read(text))
