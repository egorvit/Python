import os
import yaml
import argparse

# Инициализация парсера аргументов командной строки
parser = argparse.ArgumentParser(description="Generate Gatus templates from Ansible inventories")
parser.add_argument("--ansible-inventory", required=True, help="Path to the root directory with Ansible inventories")
parser.add_argument("--output-directory", required=True, help="Path to the directory to save Gatus templates")
parser.add_argument("--gatus-template", required=True, help="Path to the Gatus template file")

args = parser.parse_args()
ansible_inventory_root = args.ansible_inventory
output_directory = args.output_directory
gatus_template_file = args.gatus_template

# Чтение шаблона Gatus из файла
with open(gatus_template_file, "r") as gatus_template_file:
    gatus_template = gatus_template_file.read()


# Функция для генерации шаблона Gatus
def generate_gatus_template(hostname, host_data):
    host_address = host_data.get("ansible_host", "")

    if not host_address:
        return None

    return gatus_template.format(hostname=hostname, host_address=host_address)


# Функция для обхода директорий и создания шаблонов Gatus
def generate_gatus_templates(root_directory, output_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Игнорируем директории group_vars и host_vars
        if "group_vars" in dirpath or "host_vars" in dirpath:
            continue

        for filename in filenames:
            if filename.endswith((".yml", ".yaml")):
                inventory_file = os.path.join(dirpath, filename)

                with open(inventory_file, "r") as file:
                    inventory_data = yaml.safe_load(file)
                if inventory_data:
                    for group, hosts in inventory_data.items():
                        for hostname, host_data in hosts.get("hosts", {}).items():
                            gatus_template_content = generate_gatus_template(hostname, host_data)

                            if gatus_template_content:
                                output_filename = os.path.join(output_directory, f"{hostname}_gatus.yml")

                                with open(output_filename, "w") as file:
                                    file.write(gatus_template_content)

                                print(f"Создан шаблон Gatus для хоста {hostname} и сохранен в {output_filename}")


def main():
    generate_gatus_templates(ansible_inventory_root, output_directory)


if __name__ == '__main__':
    main()


