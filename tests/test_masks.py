from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("1236578513498654", "1236 57** **** 8654"),
        ("7778985612354895", "7778 98** **** 4895"),
        ("9999777788885555", "9999 77** **** 5555"),
        ("1235689789554252", "1235 68** **** 4252"),
    ],
)
def test_get_mask_card_number_right(card_num: Union[str], expected: Union[str]) -> None:
    """Тестирование функции с использованием параметризации, с готовыми 'argnames' и 'argvalues'"""
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("12365785134986", "1236 57** **** 8654"),
        ("77789856123548", "7778 98** **** 4895"),
        ("999977778888555", "9999 77** **** 5555"),
        ("123568978955", "1235 68** **** 4252"),
    ],
)
def test_get_mask_card_number_wrong(card_num: Union[str], expected: Union[str]) -> None:
    """Тестирование функции с использованием параметризации, с готовыми 'argnames' и 'argvalues'"""
    assert get_mask_card_number(card_num) != expected


def test_get_mask_card_number_with_fixt_1(mask_number: Union[str]) -> None:
    """Тестирование функции с использованием fixture"""
    assert get_mask_card_number(mask_number) == "1236 57** **** 8654"


def test_get_mask_card_number_with_fixt_2(mask_number_1: Union[str]) -> None:
    """Тестирование функции с использованием fixture"""
    assert get_mask_card_number(mask_number_1) == "7778 98** **** 4895"


def test_get_mask_card_number_with_fixt_3(mask_number_2: Union[str]) -> None:
    """Тестирование функции с использованием fixture"""
    assert get_mask_card_number(mask_number_2) != "1236 54** **** 5321"


@pytest.mark.parametrize(
    "account_num, mask_num",
    [
        ("159159", "** 9159"),
        ("123123", "** 3123"),
        ("741741", "** 1741"),
        ("888888", "** 8888"),
        ("963963", "** 3963"),
    ],
)
def test_get_mask_account(account_num: Union[str], mask_num: Union[str]) -> None:
    assert get_mask_account(account_num) == mask_num
