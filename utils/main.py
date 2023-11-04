from functions import load_operations, get_last_five_executed_operations, convert_date, requisites_mask

if __name__ == '__main__':
    file = "operations.json"

    for operation in get_last_five_executed_operations(load_operations(file)):
        print(f"{convert_date(operation['date'])} {operation['description']}")
        print(f"{requisites_mask(operation.get('from'))} -> {requisites_mask(operation.get('to'))}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
