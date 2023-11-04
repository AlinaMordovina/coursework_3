import json
from datetime import datetime


def load_operations(file):
    """Загружает список операций из файла."""

    with open(file, "r", encoding="utf-8") as operations_file:
        operations = json.load(operations_file)

    return operations


def get_last_five_executed_operations(operations):
    """Получаем последние 5 операций со статусом 'EXECUTED из cписка операций."""

    executed_operations = []

    for operation in operations:
        if operation == {}:
            continue
        elif operation['state'] == 'EXECUTED':
            executed_operations.append(operation)

    sort_executed_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)

    if len(sort_executed_operations) >= 5:
        return sort_executed_operations[0:5]
    else:
        return sort_executed_operations


def convert_date(data):
    """Преобразуем дату в формат ДД.ММ.ГГГГ."""

    convert_data = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')

    return convert_data.strftime('%d.%m.%Y')


def requisites_mask(requisite):
    """Преобразуем используемые реквизиты карты/счета в требуемый формат."""

    if requisite is None:
        return 'Неизвестно'

    else:
        number = requisite.split()[-1]
        name = requisite.split()[:-1]

        if 'Счет' in requisite:
            private_number = (len(number[14:-4]) * '*') + number[-4:]

            return " ".join(name) + " " + "".join(private_number)

        else:
            private_number = number[:6] + (len(number[6:-4]) * '*') + number[-4:]
            parts, part = len(private_number), len(private_number) // 4

            return " ".join(name) + " " + " ".join([private_number[i:i + part] for i in range(0, parts, part)])
