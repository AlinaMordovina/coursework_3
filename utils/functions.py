import json
from datetime import datetime


def load_operations(file):
    """Загружает список операций из файла."""

    with open(file, "r", encoding="utf-8") as operations_file:
        operations = json.load(operations_file)

    return operations


def get_last_five_executed_operations(file):
    """Получаем последние 5 операций со статусом 'EXECUTED из файла."""

    executed_operations = []

    for operation in load_operations(file):
        if operation == {}:
            continue
        elif operation['state'] == 'EXECUTED':
            executed_operations.append(operation)

    sort_executed_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    return sort_executed_operations[0:5]


def convert_date(data):
    """Преобразуем дату в формат ДД.ММ.ГГГГ."""

    convert_data = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')

    return convert_data.strftime('%d.%m.%Y')


def convert_card(card):
    """Преобразуем номер карты в нужный формат."""

    card_number = card.split()[-1]

    if 'Счет' in card:
        private_number = (len(card_number[14:-4]) * '*') + card_number[-4:]

        return "".join(private_number)

    else:
        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4

        return " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])


def get_name_card(card):
    """Получаем наименование карты."""

    card_name = card.split()[:-1]

    return " ".join(card_name)
