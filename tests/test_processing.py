from src.processing import count_operations_by_categories, filter_by_state, process_bank_search, sort_by_date


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


def test_count_operations_by_categories():
    """Простые тесты для count_operations_by_categories"""
    # Тест 1: Обычная работа
    transactions = [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Открытие вклада", "amount": 200},
        {"description": "Перевод с карты", "amount": 300},
    ]
    categories = ["перевод", "вклад"]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"перевод": 2, "вклад": 1}

    # Тест 2: Разный регистр
    transactions = [{"description": "ПЕРЕВОД БАНКУ", "amount": 100}, {"description": "Открытие Вклада", "amount": 200}]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"перевод": 1, "вклад": 1}

    # Тест 3: Нет совпадений - ожидаем пустой словарь
    transactions = [{"description": "Оплата услуг", "amount": 100}, {"description": "Снятие наличных", "amount": 200}]
    result = count_operations_by_categories(transactions, categories)
    assert result == {}  # Изменили ожидание на пустой словарь


def test_process_bank_search():
    transactions = [
        {"description": "Перевод в Сбербанк", "amount": 100},  # содержит "банк"
        {"description": "Оплата Тинькофф", "amount": 200},  # не содержит "банк"
        {"description": "Перевод Альфа-Банк", "amount": 300},  # содержит "банк"
        {"description": "Вклад в ВТБ", "amount": 400},  # не содержит "банк"
    ]

    # Поиск "перевод" (должен найти 2 операции)
    result = process_bank_search(transactions, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод в Сбербанк"
    assert result[1]["description"] == "Перевод Альфа-Банк"

    # Поиск "банк" (должен найти 2 операции: Сбербанк, Альфа-Банк)
    # ВТБ не содержит слово "банк" в описании.
    result = process_bank_search(transactions, "банк")
    assert len(result) == 2  # Исправлено с 3 на 2

    # Поиск "сбербанк" (должен найти 1 операцию)
    result = process_bank_search(transactions, "сбербанк")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод в Сбербанк"

    # Поиск "газпром" (не должно быть совпадений)
    result = process_bank_search(transactions, "газпром")
    assert len(result) == 0

    # Поиск в верхнем регистре "СБЕРБАНК"
    result = process_bank_search(transactions, "СБЕРБАНК")
    assert len(result) == 1

    # Поиск "втб" (должен найти 1 операцию)
    result = process_bank_search(transactions, "втб")
    assert len(result) == 1
