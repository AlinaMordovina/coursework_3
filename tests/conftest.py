import pytest


@pytest.fixture
def operations_fixture():
    operations = [{
        "id": 871921546,
        "state": "EXECUTED",
        "date": "2019-02-14T03:09:23.006652",
        "operationAmount": {
            "amount": "47022.09",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Classic 6216537926639975",
        "to": "Счет 67667879435628279708"
        },
        {
        "id": 260972664,
        "state": "EXECUTED",
        "date": "2018-01-23T01:48:30.477053",
        "operationAmount": {
            "amount": "2974.30",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие счета",
        "to": "Visa Gold 2684274847577419"
        },
        {
        "id": 317987878,
        "state": "EXECUTED",
        "date": "2018-01-13T13:00:58.458625",
        "operationAmount": {
            "amount": "55985.82",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 8906171742833215",
        "to": "Visa Platinum 6086997013848217"
        },
        {
        "id": 72122709,
        "state": "EXECUTED",
        "date": "2018-01-11T17:07:09.800800",
        "operationAmount": {
            "amount": "19683.25",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 86675623828180311969",
        "to": "Счет 15351391408911677994"
        },
        {
        "id": 286706711,
        "state": "EXECUTED",
        "date": "2018-01-06T06:42:02.219233",
        "operationAmount": {
            "amount": "621.37",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 9175985085449563",
        "to": "Счет 82781399328834147668"
        },
        {},
        {
        "id": 464419177,
        "state": "CANCELED",
        "date": "2018-07-15T18:44:13.346362",
        "operationAmount": {
            "amount": "71024.64",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Gold 9657499677062945",
        "to": "Счет 19213886662094884261"
        }]

    return operations.copy()
