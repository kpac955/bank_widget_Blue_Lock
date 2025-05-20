from unittest.mock import patch

from src.external_api import convert


@patch("src.external_api.requests.get")
def test_convert(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 80}}

    # Создаем конвертацию валюты для
    # USD
    usd = {"amount": 5, "currency": "USD"}
    assert convert(usd) == 400.0
    # EUR
    eur = {"amount": 20, "currency": "EUR"}
    assert convert(eur) == 1600.0
    # RUB
    rub = {"amount": 4500, "currency": "RUB"}
    assert convert(rub) == 4500.0
    # при неизвестной валюте получаем - 0.0
    nn = {"amount": 200, "currency": "NN"}
    assert convert(nn) == 0.0
