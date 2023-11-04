from utils import functions


def test_load_operations():
    assert functions.load_operations("operations_test.json") == [{
      "id": 720751477,
      "state": "EXECUTED",
      "date": "2018-11-08T08:21:45.902633",
      "operationAmount": {
        "amount": "16872.46",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Счет 75743795418434298755",
      "to": "Счет 80785963509390811744"
    }]


def test_get_last_five_executed_operations(operations_fixture):
    assert functions.get_last_five_executed_operations(operations_fixture) == [{
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
      }]
    assert functions.get_last_five_executed_operations([{}, {}]) == []
    assert functions.get_last_five_executed_operations([{
        "id": 871921546,
        "state": "EXECUTED",
        "date": "2019-02-14T03:09:23.006652",
        "operationAmount": {
            "amount": "47022.09",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }}]) == [{
            "id": 871921546,
            "state": "EXECUTED",
            "date": "2019-02-14T03:09:23.006652",
            "operationAmount": {
                "amount": "47022.09",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }}]
    assert functions.get_last_five_executed_operations([{
        "id": 871921546,
        "state": "CANCELED",
        "date": "2019-02-14T03:09:23.006652",
        "operationAmount": {
            "amount": "47022.09",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }}]) == []


def test_convert_date():
    assert functions.convert_date("2019-02-14T03:09:23.006652") == "14.02.2019"
    assert functions.convert_date("2018-01-23T01:48:30.477053") == "23.01.2018"


def test_requisites_mask():
    assert functions.requisites_mask("Visa Gold 2684274847577419") == "Visa Gold 2684 27** **** 7419"
    assert functions.requisites_mask("Счет 86675623828180311969") == "Счет **1969"
    assert functions.requisites_mask(None) == 'Неизвестно'
