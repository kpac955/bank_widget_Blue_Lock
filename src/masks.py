from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Прописываем функцию маскировки номера банковской карты клиента"""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Прописываем функцию маскировки номера счета клиента"""
    return f"** {account_number[-4:]}"
