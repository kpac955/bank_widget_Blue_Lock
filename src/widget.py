from masks import get_mask_card_number, get_mask_account


def mask_account_card(type_and_number: str) -> str:
    """ Функция, которая маскирует номер счета или карты"""
    if 'Счет' in type_and_number:
        return f'Счет {get_mask_account(type_and_number[-5:])}'
    else:
        return f'{type_and_number[:-16]} {get_mask_card_number(type_and_number[-16:])}'



