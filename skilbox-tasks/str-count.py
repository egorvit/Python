import os
from collections.abc import Iterable


def gen_func(path: str) -> Iterable[tuple]:
    count_line = 0
    for link, dirs, files in list(os.walk(path)):
        for file in files:
            if os.path.isfile(os.path.abspath(os.path.join(path, file))) and file.endswith('.py'):
                with open(os.path.abspath(os.path.join(path, file)), 'r') as f:
                    for string in f.readlines():
                        if string != '\n' and '#' not in string:
                            count_line += 1
                    yield os.path.join(path, file), count_line


user_path = input('Введите директорию: ')
for result in gen_func(user_path):
    print(result)