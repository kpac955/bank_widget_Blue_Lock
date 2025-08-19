from typing import Dict, Any
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date
from src.csv_operations import read_csv_operations
from src.xlsx_operations import read_xlsx_operations
from src.external_api import convert


def normalize_answer(answer: str) -> bool:
    """Приводит ответ к булеву значению с учетом разных регистров"""
    return answer.strip().lower() in ["да", "yes", "y", "д", "yes", "y", "true", "1"]


def get_amount_from_transaction(transaction: Dict[str, Any]) -> str:
    """Извлекает сумму транзакции"""
    amount = transaction.get('operationAmount', {}).get('amount', '0')
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('name', '')

    if currency:
        return f"{amount} {currency}"
    return f"{amount}"


def format_transaction(transaction: Dict[str, Any]) -> str:
    """Форматирует транзакцию для вывода."""

    date = get_date(transaction.get('date', ''))
    description = transaction.get('description', '')

    # Обработка отправителя и получателя
    from_info = transaction.get('from', '')
    to_info = transaction.get('to', '')

    # Используем mask_account_card вместо отдельных функций
    from_display = mask_account_card(from_info) if from_info else "Не указано"
    to_display = mask_account_card(to_info) if to_info else "Не указано"

    # Получаем сумму
    amount_info = get_amount_from_transaction(transaction)

    # Формирование результата
    result = f"{date} {description}\n"

    if from_info and to_info:
        result += f"{from_display} -> {to_display}\n"
    elif from_info:
        result += f"{from_display}\n"
    elif to_info:
        result += f"-> {to_display}\n"

    result += f"Сумма: {amount_info}"

    return result


