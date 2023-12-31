from settings import OPERATIONS
from functions import json_to_list, del_empty, split_dict, output_format


def main():
    """
    На вход получаем данные из файла в фомрате  json

     Выводим на экран список из 5 последних выполненных клиентом операций

     Формат вывода данных:
     <дата перевода> <описание перевода>
     <откуда> -> <куда>
     <сумма перевода> <валюта>

     Между операциями должна быть пустая строка
     Сверху - последние по дате операции
     Номер карты замаскирован в формате: ХХХХ ХХ** **** ХХХХ
     Номер счета замаскирован в формате: **ХХХХ
    """

    # Загружаем данные из файла в словарь
    all_data_list = json_to_list(OPERATIONS)

    # Удаляем пустые операции
    all_data_list = del_empty(all_data_list)

    # Убираем из словаря лишнюю информацию, оставляем только 5 операций, отсортированных по дате
    five_operations = split_dict(all_data_list, 5)

    # Выводим данные в нужном формате
    print((output_format(five_operations)))


if __name__ == '__main__':
    main()
