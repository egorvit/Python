from sys import argv
import os
import re

"""Берем аргументы из командной строки. 
    Формируем универсальные пути до файлов."""

lst_of_argv = argv
first_path = os.path.join(lst_of_argv[1])
second_path = os.path.join(lst_of_argv[2])


def use_regex(input_text):
    """Проходим по тексту и удаляем не интересующие нас данные: время, дата, путь."""

    new_text = re.sub(r"/[^,\s]+,?", '', input_text)
    new_text = re.sub(r'\d\d-\d\d-\d{4}', '', new_text)
    new_text = re.sub(r'\d\d:\d\d:\d\d', '', new_text)
    return new_text


def diff(first_file, second_file):
    """Открываем файлы и передаем их в функцию use_regex.
    Возвращает различие между двумя текстами."""

    with open(first_file) as file_one, open(second_file) as file_two:
        text_first = use_regex(file_one.read()).split('\n')
        text_second = use_regex(file_two.read()).split('\n')
        return set(text_first) ^ set(text_second)


def main():
    """Выводим результат на экран."""

    result = diff(first_path, second_path)

    if result:
        print('Различающиеся строки:')
        num = 1
        for string in result:
            print(num, '--', string)
            num += 1
    else:
        print('Файлы отличаются только временем и местом сборки.')


if __name__ == '__main__':
    main()
