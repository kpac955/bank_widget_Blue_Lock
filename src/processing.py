from typing import Dict, List


def filter_by_state(list_dict: List[Dict], opt_value: str = "EXECUTED") -> List[Dict]:
    """Функция, которая возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    new_list_dict = []
    for every_dict in list_dict:
        if every_dict["state"] == opt_value:
            new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date(list_dict: List[Dict], arg_sort: bool = True) -> List[Dict]:
    """Функция, которая возвращает новый список, отсортированный по дате"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_sort)
    return sort_list
