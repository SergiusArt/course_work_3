import json
from datetime import datetime


def json_to_list(path_name) -> list:
    """
    Загружает данные из json файла в словарь
    :return: [list]
    """

    with open(path_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def del_empty(list_load):
    """
    Удаляет пустые словари
    :param list_load: исследуемый список
    :return: новый список без пустых элементов
    """

    new_list = []

    for item in list_load:
        if len(item) > 0:
            new_list.append(item)

    return new_list


def split_dict(data_list, number):
    """
    Формируем новый словарь по последним значениям из загруженного
    :param data_list: загруженный список с данными
    :param number: количество крайних значений
    :return: список с указанным количеством крайних значений
    """

    new_list = []
    sort_list = sorted(data_list, key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    for i in range(number):
        new_list.append(sort_list[i])

    return new_list


def output_format(operations):
    """
    Печатает отформатированные данные
    :param operations: список операций
    """

    new_str_list = []

    for operation in operations:

        # Если какая-то информации нет в данных - пишем "отсутствуют данные"
        if not "id" in operation:
            operation["id"] = '[отсутствуют данные]'
        if not "state" in operation:
            operation["state"] = '[отсутствуют данные]'
        if not "date" in operation:
            operation["date"] = '[отсутствуют данные]'

        if not "operationAmount" in operation:
            operation["operationAmount"]['amount'] = '[отсутствуют данные]'
            operation["operationAmount"]['currency']["name"] = '[отсутствуют данные]'
            operation["operationAmount"]['amount']["code"] = '[отсутствуют данные]'
        else:
            if not 'amount' in operation[ "operationAmount"]:
                operation["operationAmount"]['amount'] = '[отсутствуют данные]'

        if not "currency" in operation[ "operationAmount"]:
            operation["operationAmount"]['currency']["name"] = '[отсутствуют данные]'
            operation["operationAmount"]['amount']["code"] = '[отсутствуют данные]'
        else:
            if not "name" in operation[ "operationAmount"]['currency']:
                operation["operationAmount"]['currency']["name"] = '[отсутствуют данные]'
            if not "code" in operation[ "operationAmount"]['currency']:
                operation["operationAmount"]['currency']["code"] = '[отсутствуют данные]'

        if not "description" in operation:
            operation["description"] = '[отсутствуют данные]'
        if not "from" in operation:
            operation["from"] = '[отсутствуют данные]'
        if not "to" in operation:
            operation["to"] = '[отсутствуют данные]'

        date_obj = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
        from_count = ""

        # Если данные "from" в наличии, то форматируем их, иначе пишем, что отсутствуют данные
        if operation["from"] != '[отсутствуют данные]':

            for i in reversed(range(len(operation["from"]))):
                if operation["from"][i] != " ":
                    from_count = from_count + operation["from"][i]
                else:
                    from_count = ''.join(reversed(from_count))
                    break
            from_card = " ".join(operation["from"].split(' ')[:-1])
            from_count = from_count[0:4] + ' ' + from_count[4:6] + '** **** ' + from_count[-4:]
        else:
            from_card = '[отсутствуют данные]'
            from_count = '[отсутствуют данные]'

        # Если данные "to" в наличии, то форматируем их, иначе пишем, что отсутствуют данные
        if operation['to'] != '[отсутствуют данные]':
            to_count = '**' + "".join(operation["to"].split(' ')[-1][-4:])
        else:
            to_count = '[отсутствуют данные]'

        if from_card and from_count == '[отсутствуют данные]':
            from_count = ''

        # В остальных случаях, выводим отформатированное сообщение
        # Если где-то данных нет, то указываем ['отсутствуют данные']

        new_str_list.append(f'{date_obj.strftime("%d.%m.%Y")} {operation["description"]}\n' \
               f'{from_card} {from_count} -> Счет {to_count}\n' \
               f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')

    return '\n'.join(new_str_list)
