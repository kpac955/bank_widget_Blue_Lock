import re
from collections import Counter
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



def count_operations_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает операции по категориям из описания."""
    category_counter = Counter()
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for categorie in categories:
            if categorie.lower() in description:
                category_counter[categorie] += 1
    return dict(category_counter)


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество операций по каждой категории на основе описания."""
    category_counts = Counter()

    for operation in data:
        description = operation.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1

    return dict(category_counts)


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """Ищет банковские операции по заданной строке.
    Возвращает список операций, где найдено совпадение"""
    if not data or not search:
        return []

    try:
        # Создаем регулярное выражение для поиска (без учета регистра)
        search_re = re.compile(search, re.IGNORECASE)
    except re.error:
        # Если передан некорректный паттерн - возвращаем пустой список
        return []

    match_in_descriptions = []

    for operation in data:
        # Проверяем, что operation - словарь и содержит описание
        if isinstance(operation, dict) and "description" in operation:
            description = operation["description"]
            # Проверяем, что описание - строка и есть совпадение
            if isinstance(description, str) and search_re.search(description):
                match_in_descriptions.append(operation)

    return match_in_descriptions
