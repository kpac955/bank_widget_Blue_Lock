from typing import Iterator


def filter_by_currency(transaction_list: list[dict], code_of_currency: str) -> Iterator:
    """Функция возвращает итератор, где валюта соответствует заданной в параметре"""
    if not transaction_list:
        raise TypeError("Список транзакций пустой!")

    filtred_transactions = filter(
        lambda transaction: transaction.get("operationAmount").get("currency").get("code") == code_of_currency,
        transaction_list,
    )
    return filtred_transactions


def transaction_descriptions(transaction_list: list[dict]) -> Iterator:
    """Функция возвращает описания для транзакций"""
    for transaction in transaction_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров карт формата 'ХХХХ ХХХХ ХХХХ ХХХХ' в заданном числовом диапозоне"""
    if not isinstance(start, (int | float)) or not isinstance(stop, (int | float)):
        raise TypeError("Ошибка типа данных")
    for x in range(start, stop + 1):
        card_number = f"{x:016}"
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
