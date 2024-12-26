from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    """ Функция, которая маскирует номер счета или карты"""
    if 'Счет' in type_and_number:
        return f'Счет {get_mask_account(type_and_number[-6:])}'
    else:
        return f'{type_and_number[:-16]} {get_mask_card_number(type_and_number[-16:])}'


def get_date(data: str) -> str:
    return f'{data[8:10]}.{data[5:7]}.{data[0:4]}'
