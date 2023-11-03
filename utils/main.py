from functions import get_last_five_executed_operations, convert_date, convert_card, get_name_card

if __name__ == '__main__':
    file = "operations.json"

    for num in get_last_five_executed_operations(file):
        if 'from' not in num:
            print(f"""{convert_date(num['date'])} {num['description']}
-> {get_name_card(num['to'])} {convert_card(num['to'])}
{num['operationAmount']['amount']} {num['operationAmount']['currency']['name']}
""")
        else:
            print(f"""{convert_date(num['date'])} {num['description']}
{get_name_card(num['from'])} {convert_card(num['from'])} -> {get_name_card(num['to'])} {convert_card(num['to'])}
{num['operationAmount']['amount']} {num['operationAmount']['currency']['name']}
""")
