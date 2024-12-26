from typing import Union

card_number = input()
account_number = input()


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Прописываем функцию маскировки номера банковской карты клиента"""
    str_card_number = str(card_number)
    return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[12:]} "


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Прописываем функцию маскировки номера счета клиента"""
    str_account_number = str(account_number)
    return f"** {str_account_number[2:]}"
