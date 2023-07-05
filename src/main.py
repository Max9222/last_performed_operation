
import utils
from colorama import Fore

FILE_JSON = "operations.json"

def main():
    """
    Функция читает файл Json, сортирует список и выводит на экран список из 5 последних выполненных клиентом операций в формате:
    <дата перевода><описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    :return:
    """
    load_file = utils.load_operations(FILE_JSON)

    dictionary = utils.read_data_time(load_file)

    dictionary_five = dictionary[0:5]
    for i in dictionary_five:
        print(Fore.BLUE + "")
        print(f'{i[0].day}-{i[0].month}-{i[0].year} {i[2]}')
        print(f"{i[1][0:-12]}****** -> {i[1][:4]} **{i[1][-4:]}")
        print(f"{i[4]['amount']} {i[4]['currency']['name']}")
        print()

if __name__ == '__main__':

    main()