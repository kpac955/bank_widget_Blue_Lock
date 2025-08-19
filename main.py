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


def main() -> None:
    """Основная функция программы"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")

    # Ввод пользователя
    user_choice = input("Пользователь: ").strip()

    # Чтение файла
    file_paths = {
        "1": ("JSON", "data/operations.json", convert),
        "2": ("CSV", "data/transactions.csv", read_csv_operations),
        "3": ("XLSX", "data/transactions_excel.xlsx", read_xlsx_operations)
    }

    if user_choice not in file_paths:
        print("Неверный выбор. Программа завершена")
        return

    file_type, default_path, reader_func = file_paths[user_choice]
    print(f"Для обработки выбран {file_type}-файл.")

    file_path = input(f'Введите путь к {file_type}-файлу: ').strip() or default_path

    transactions = reader_func(file_path)

    if not transactions:
        print("Файл не найден или не содержит данных")
        return

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(available_statuses)}")

        user_state = input("Пользователь: ").strip().upper()

        if user_state in available_statuses:
            print(f'Операции отфильтрованы по статусу "{user_state}"')
            filtered_transactions = filter_by_state(transactions, user_state)
            break
        else:
            print(f'Статус операции "{user_state}" недоступен.')

    # Сортировка по дате
    if normalize_answer(input("\nОтсортировать операции по дате? Да/Нет: ")):
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order in ["по убыванию", "убыванию", "desc", "d"]
        filtered_transactions = sort_by_date(filtered_transactions, reverse)

    # Фильтрация по валюте
    if normalize_answer(input("\nВыводить только рублевые транзакции? Да/Нет: ")):
        filtered_transactions = [t for t in filtered_transactions
                                 if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

    # Фильтрация по ключевому слову
    if normalize_answer(input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ")):
        keyword = input("Введите слово для поиска: ").strip().lower()
        filtered_transactions = [t for t in filtered_transactions
                                 if keyword in t.get('description', '').lower()]

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...\n")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    for transaction in filtered_transactions:
        print(format_transaction(transaction))
        print()


if __name__ == "__main__":
    main()


