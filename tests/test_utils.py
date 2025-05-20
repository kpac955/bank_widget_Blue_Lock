import json

from src.utils import load_data_transactions


def test_load_valid_list_of_dicts(tmp_path):
    # Создаем JSON - файл
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(test_data), encoding="utf-8")

    # Проверка загрузки списка
    result = load_data_transactions(str(file_path))
    assert result == test_data


# Проверка что JSON не список
def test_js_not_list(tmp_path):
    test_data = {"id": 1, "amount": 10}  # словарь
    file_path = tmp_path / "test1.json"
    file_path.write_text(json.dumps(test_data), encoding="utf-8")

    result = load_data_transactions(str(file_path))
    assert result == []


# Проверка что JSON не правильный
def test_json_invalid(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{wwwrrrrwwww}", encoding="utf-8")

    result = load_data_transactions(str(file_path))
    assert result == []


# Проверка на то что файл не существует
def file_not_found():
    result = load_data_transactions("здесь что-то есть")  # такого файла нет
    assert result == []
