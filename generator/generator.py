import random
import string

def generate_random_text(size_in_bytes):
    # Генерируем случайный текст, состоящий из букв латинского алфавита (в верхнем и нижнем регистре)
    # и пробелов, чтобы получить текстовый файл.
    characters = string.ascii_letters + " "
    random_text = ''.join(random.choice(characters) for _ in range(size_in_bytes))
    return random_text

def write_to_file(file_path, content):
    # Записываем содержимое в файл.
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Размер файла в байтах (1 МБ = 1 048 576 байт).
    file_size_bytes = 1048576

    # Генерируем случайный текст нужного размера.
    random_text = generate_random_text(file_size_bytes)

    # Указываем путь к файлу, который будет создан.
    file_path = "test_file.txt"

    # Записываем содержимое в файл.
    write_to_file(file_path, random_text)

    print(f"Тестовый файл {file_path} размером в 1 мегабайт создан успешно.")