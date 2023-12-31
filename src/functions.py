import json

import datetime


def load_operations(file='operations.json'):
    """
    Загружает список банковсих операций из файла "operations.json"
    :file: Файл для чтения
    :return: Возвращает список банковсих операций
    """
    list_of_operations = ''

    with open(file, 'r', encoding='UTF=8') as file:
        for line in file:
            list_of_operations += line

    list_of_operations = json.loads(list_of_operations)

    return list_of_operations


def after_of_operations(operations,number_of_operation=-5):
    """
    Получает список банковсих операций из функции "load_operations()"
    :operations: Данные по банковсой операции
    :number_of_operation: Количесвто операцый для вывода
    :return: Возвращает список последних операций
    """
    list_of_operations = []
    last_5_list_of_operations = []

    for operation in operations:
        if "date" not in operation:
            continue

        if operation["state"] == 'CANCELED':
            continue

        else:
            date_of_operation = datetime.date(day=int(operation["date"][8:10]), month=int(operation["date"][5:7]),
                                              year=int(operation["date"][0:4]))
            list_of_operations.append(date_of_operation)

        list_of_operations = sorted(list_of_operations)
        last_5_list_of_operations = list_of_operations[number_of_operation:]
        last_5_list_of_operations.reverse()

    return last_5_list_of_operations


def slices_by_operation(check_and_card):
    """
    Получает список банковсих операций из функции "load_operations()"
    :check_and_card: Номер и банк карты
    :return: Возвращает замаскированный номер карты и ее банк
    """
    # Записывает замаскированный номер карты
    to_operation = (check_and_card[-16:-12] + " " + check_and_card[-12:-10] +
                    '** **** ' + check_and_card[-4:])

    # Добавляет к записанному замаскированному номеру карты ее банк
    if "Maestro" in check_and_card:
        to_operation = "Maestro " + to_operation

    elif "МИР" in check_and_card:
        to_operation = "МИР " + to_operation

    elif "Visa Classic" in check_and_card:
        to_operation = "Visa Classic " + to_operation

    elif "Visa Platinum" in check_and_card:
        to_operation = "Visa Platinum " + to_operation

    elif "Visa Gold" in check_and_card:
        to_operation = "Visa Gold " + to_operation

    elif "MasterCard" in check_and_card:
        to_operation = "MasterCard " + to_operation

    elif "Счет" in check_and_card:
        to_operation = check_and_card[0:5] + '**' + check_and_card[-4:]

    return to_operation
