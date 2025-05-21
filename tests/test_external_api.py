from unittest.mock import patch

from src.external_api import convert


@patch("src.external_api.requests.get")
def test_convert(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 400.0}
    # Создаем конвертацию валюты для
    # USD
    usd = {"operationAmount": {"amount": 5, "currency": {"name": "USD", "code": "USD"}}}
    assert convert(usd) == 400.0

    mock_get.return_value.json.return_value = {"result": 1600.0}
    # EUR
    eur = {"operationAmount": {"amount": 20, "currency": {"name": "EUR", "code": "EUR"}}}
    assert convert(eur) == 1600.0

    # RUB
    rub = {"operationAmount": {"amount": "4500", "currency": {"name": "RUB", "code": "RUB"}}}
    assert convert(rub) == 4500.0

    # Не определена
    nn = {"operationAmount": {"amount": "200", "currency": {"name": "None", "code": "NN"}}}
    assert convert(nn) == 0.0
