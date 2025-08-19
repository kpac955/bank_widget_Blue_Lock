from src.processing import filter_by_state, sort_by_date, count_operations_by_categories


def test_filter_right_by_state(right_date: list[dict]) -> None:
    assert filter_by_state(right_date) == [
        {"id": 56521548, "state": "EXECUTED", "date": "2019-09-02T13:35:58.425572"},
        {"id": 565215485, "state": "EXECUTED", "date": "1994-08-11T12:37:58.425572"},
    ]


def test_filter_wrong_by_state(wrong_date: list[dict]) -> None:
    assert filter_by_state(wrong_date) == [
        {"id": 45678922, "state": "EXECUTED", "date": "hjkuytghj"},
        {"id": 789954562, "state": "EXECUTED", "date": "*******"},
    ]


def test_sort_by_date(sort_date: list[dict]) -> None:
    assert sort_by_date(sort_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_count_operations_by_categories_basic():
    """Простые тесты для count_operations_by_categories"""
    # Тест 1: Обычная работа
    transactions = [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Открытие вклада", "amount": 200},
        {"description": "Перевод с карты", "amount": 300}
    ]
    categories = ["перевод", "вклад"]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"перевод": 2, "вклад": 1}

    # Тест 2: Разный регистр
    transactions = [
        {"description": "ПЕРЕВОД БАНКУ", "amount": 100},
        {"description": "Открытие Вклада", "amount": 200}
    ]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"перевод": 1, "вклад": 1}

    # Тест 3: Нет совпадений
    transactions = [
        {"description": "Оплата услуг", "amount": 100},
        {"description": "Снятие наличных", "amount": 200}
    ]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"перевод": 0, "вклад": 0}

    # Тест 4: Пустые данные
    assert count_operations_by_categories([], categories) == {"перевод": 0, "вклад": 0}
    assert count_operations_by_categories(transactions, []) == {}