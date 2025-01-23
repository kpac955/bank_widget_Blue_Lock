from typing import Union

import pytest


@pytest.fixture()
def acc_mask() -> Union[str]:
    return "Счет 1111300734726758"


@pytest.fixture()
def mask_number() -> Union[str]:
    return "1236578513498654"


@pytest.fixture()
def mask_number_1() -> Union[str]:
    return "7778985612354895"


@pytest.fixture()
def mask_number_2() -> Union[str]:
    return "1236548954235"


# Фикстуры для модуля processing.py -> для функции filter_by_state
@pytest.fixture()
def right_date() -> list[dict]:
    return [
        {"id": 56521548, "state": "EXECUTED", "date": "2019-09-02T13:35:58.425572"},
        {"id": 565215485, "state": "EXECUTED", "date": "1994-08-11T12:37:58.425572"},
    ]


@pytest.fixture()
def wrong_date() -> list[dict]:
    return [
        {"id": 45678922, "state": "EXECUTED", "date": "hjkuytghj"},
        {"id": 789954562, "state": "EXECUTED", "date": "*******"},
        {"id": 896545355, "state": "CANCELED", "date": "-----"},
        {"id": 659845516, "state": "CANCELED", "date": " "},
    ]


# для функции sort_by_date
@pytest.fixture()
def sort_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
