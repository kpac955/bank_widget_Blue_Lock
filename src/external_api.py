# импортируем необходимые для работы модули, библиотеки, функции.
import os
from typing import Dict

import requests
from dotenv import load_dotenv

# загрузка переменных из файла .env
load_dotenv()

URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
API_KEY = os.getenv("API_KEY")


def convert(transactions: Dict[str, object]) -> float:
    # Выполняет перевод суммы транзакции в рубли
    # Если USD, EUR, то идет обращение к API сервису

    # получаем ключ из словаря transactions
    # если его нет или что то не является словарем - возвращаем ноль
    operation = transactions.get("operationAmount", {})
    if not isinstance(operation, dict):
        return 0.0

    # извлекаем "amount" из словаря operation и приводим ее к float
    # при неверном значении выводим ноль
    amount_to = operation.get("amount", "0")
    try:
        amount = float(amount_to)
    except(ValueError, TypeError):
        return 0.0
    # извлекаем "currency" из словаря operation
    # если не словарь - возвращаем 0.0
    currency_data = operation.get("currency", {})
    if not isinstance(currency_data, dict):
        return 0.0

    currency = str(currency_data.get("code", "RUB")).upper()

    # Если транзакция в рублях, то функция просто возвращает данную сумму
    if currency == "RUB":
        return amount
    # Если транзакция не в RUB, EUR, USD  возвращаем 0.0
    if currency not in ("USD", "EUR"):
        return 0.0

    headers = {"apikey": API_KEY}
    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }
    try:
        response = requests.get(URL, headers=headers, params=params)
        data = response.json()
        result = data.get("result")
        return float(result) if result is not None else 0.0
    except (requests.RequestException, ValueError, TypeError):
        return 0.0
