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
    amount = float(transactions.get("amount", 0))
    currency = str(transactions.get("currency", "RUB")).upper()
    # Если транзакция в рублях, то функция просто возвращает данную сумму
    if currency == "RUB":
        return amount
    # Если транзакция не в RUB, EUR, USD  возвращаем 0.0
    if currency not in ("USD", "EUR"):
        return 0.0
    else:
        headers = {"apikey": API_KEY}

        params = {"base": currency, "symbols": "RUB"}

    response = requests.get(URL, headers=headers, params=params)
    data = response.json()
    rate = data.get("rates").get("RUB")

    if rate is None:
        return 0.0

    return amount * rate
