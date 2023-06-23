from course_work_3.functions import json_to_list, del_empty, split_dict, output_format
from course_work_3.settings import ROOT
from pathlib import Path


def test_json_to_list():
    """
    Информация из json файла должна загрузиться во вложенный список
    """

    assert json_to_list(Path.joinpath(ROOT.parent, 'tests/for_test_json_data.json')) == [
  {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {
      "amount": "48150.39",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655"
  },
  {},
  {
    "id": 108066781,
    "state": "EXECUTED",
    "date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90817634362091276762"
  },
      {
        "id": 108326781,
        "state": "EXECUTED",
        "date": "2019-06-21T12:34:06.351022",
        "operationAmount": {
          "amount": "25762.92",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Открытие вклада"
      }
]

def test_del_empty():
  """
  Пустые словари должны удалиться
  """
  assert del_empty(json_to_list(Path.joinpath(ROOT.parent, 'tests/for_test_json_data.json'))) == [
  {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {
      "amount": "48150.39",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655"
  },
  {
    "id": 108066781,
    "state": "EXECUTED",
    "date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90817634362091276762"
  },
  {
    "id": 108326781,
    "state": "EXECUTED",
    "date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада"
  }
]

def test_split_dict():
  """
  Форминуется новый список из обработанного с указанным количеством операций
  """
  assert split_dict(del_empty(json_to_list(Path.joinpath(ROOT.parent, 'tests/for_test_json_data.json'))), 2) == [
  {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {
      "amount": "48150.39",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655"
  },
  {
    "id": 108066781,
    "state": "EXECUTED",
    "date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90817634362091276762"
  }
]

def test_output_format():
  """
  Выводит информацию в нужном формате
  """

  assert output_format(split_dict(del_empty(json_to_list(Path.joinpath(ROOT.parent, 'tests/for_test_json_data.json'))), 1)) == """07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD
"""

  assert output_format(
    split_dict(del_empty(json_to_list(Path.joinpath(ROOT.parent, 'tests/for_test_json_data.json'))), 2)) == """07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

21.06.2019 Открытие вклада
[отсутствуют данные]  -> Счет **6762
25762.92 руб.
"""

  assert output_format(
    split_dict(del_empty(json_to_list(Path.joinpath(ROOT.parent, 'tests/for_test_json_data.json'))), 3)) == """07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

21.06.2019 Открытие вклада
[отсутствуют данные]  -> Счет **6762
25762.92 руб.

21.06.2019 Открытие вклада
[отсутствуют данные]  -> Счет [отсутствуют данные]
25762.92 руб.
"""