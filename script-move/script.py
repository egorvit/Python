import os
import shutil
import argparse


def create_directory_structure(src_dir, dest_dir, max_depth):
    """
    Создает аналогичную иерархию каталогов в другом каталоге.

    :param src_dir: путь к исходному каталогу
    :param dest_dir: путь к целевому каталогу
    :param max_depth: максимальный уровень вложенности, который нужно скопировать
    """
    # Удаляем целевую директорию перед копированием
    shutil.rmtree(dest_dir, ignore_errors=True)

    for root, dirs, files in os.walk(src_dir):
        # Получаем относительный путь к текущему каталогу
        rel_path = os.path.relpath(root, src_dir)
        # Разбиваем относительный путь на отдельные части
        rel_parts = rel_path.split(os.sep)
        # Если текущий уровень вложенности больше максимального,
        # то пропускаем этот каталог и все его подкаталоги
        if len(rel_parts) > max_depth:
            continue
        if len(rel_parts) == 2:
            new_file = os.path.join(dest_dir, rel_parts[-2], f"{rel_parts[-1]}.yaml")
            with open(new_file, 'w') as f:
                f.write(f"""
                \n- hosts: all\n  become: true\n  become_method: sudo\n  gather_facts: true\n  roles:\n    - ../{rel_parts[-2]}/{rel_parts[-1]}\n""")
                continue
        # Создаем новый каталог в целевом каталоге
        dest_path = os.path.join(dest_dir, rel_path)

        # Проверяем наличие файла или директории в целевой директории и удаляем их
        if os.path.exists(dest_path):
            if os.path.isfile(dest_path):
                os.remove(dest_path)
            else:
                shutil.rmtree(dest_path)

        os.makedirs(dest_path, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Create a directory structure with limited depth.")
    parser.add_argument("base_dir", type=str, help="Path to the source directory")
    args = parser.parse_args()
    src_dir = os.path.join(args.base_dir, 'roles')
    dest_dir = os.path.join(args.base_dir, 'playbook_roles')
    max_depth = 2
    create_directory_structure(src_dir, dest_dir, max_depth)


if __name__ == '__main__':
    main()