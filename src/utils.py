import json
import datetime

def load_operations(file):
    """
    Чтение файла со списком операций
    :param file:
    :return profile:
    """
    with open(file, "r", encoding='utf-8') as json_file:
        profile = json.load(json_file)
        return profile


def read_data_time(file):
    """
    Переводит к виду datatime, получаем значения по ключам и сортирует "date
    :param file: список словарей
    :return: получаем отсортированный список
    """
    date_all = []
    for info in file:
        if info.get("date", None):
            data_time_str = " ".join(info["date"].split("T"))
            to_info = info.get("to", None)
            description_info = info.get("description", None)
            from_info = info.get("from")
            amount_info = info.get("operationAmount", None)
            data_time_obj = datetime.datetime.strptime(data_time_str, '%Y-%m-%d %H:%M:%S.%f')
            date_all.extend([[data_time_obj, to_info, description_info, from_info, amount_info]])
            sorted_date_all = sorted(date_all, reverse=True)
    return sorted_date_all
