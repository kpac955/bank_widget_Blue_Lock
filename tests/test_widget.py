from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "received, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(received: Union[str], result: list[dict]) -> None:
    assert mask_account_card(received) == result


def test_mask_account_card_1(acc_mask: Union[str]) -> None:
    assert mask_account_card(acc_mask) == "Счет ** 6758"


@pytest.mark.parametrize(
    "time_in, time_out", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2019-09-02T13:35:11.671407", "02.09.2019")]
)
def test_get_date(time_in: Union[str], time_out: Union[str]) -> None:
    assert get_date(time_in) == time_out
