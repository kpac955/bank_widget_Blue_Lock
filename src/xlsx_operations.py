import logging
import os
from datetime import datetime
from typing import List, Optional, TypedDict

import pandas as pd

logging.basicConfig(level=logging.INFO)


class Operation(TypedDict):
    id: int
    state: str
    date: datetime
    amount: float
    currency_name: str
    currency_code: str
    from_account: Optional[str]
    to_account: str
    description: str


def read_xlsx_operations(file_path: str) -> List[Operation]:
    """Читает Excel файл и возвращает список словарей"""

    logging.info(f"Идет чтение файла {file_path}")

    try:

        df = pd.read_excel(file_path, engine="openpyxl")

        operations = []

        for index, row in df.iterrows():
            try:
                operation = {
                    "id": int(row["id"]),
                    "state": row["state"],
                    "date": pd.to_datetime(row["date"]),  # pandas сам поймает формат и преобразует
                    "amount": float(row["amount"]),
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from_account": row["from"] or None,
                    # row.get("from") if pd.notna(row.get("from")) else None,
                    "to_account": row["to"],
                    "description": row["description"],
                }
                operations.append(operation)
                logging.info(f"Операция с id {operation['id']} прочитана успешноб строка {index+2}")
            except (ValueError, KeyError, TypeError) as e:
                logging.warning(f"Ошибка обработки строки {index+2}: {str(e)}. Данные: {row.to_dict()}")

    except FileNotFoundError:
        logging.info(f"Файл {file_path} не найден")
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except Exception as e:
        logging.info(f"Ошибка при чтении файла {str(e)}")
        raise Exception(f"Ошибка при чтении файла {str(e)}")

    logging.info(f"Работа с файлом завершена. Всего прочитано: {len(operations)}")
    return operations


if __name__ == "__main__":
    """Определяем путь до файла Excel и запускаем функцию считывания"""
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "transactions_excel.xlsx")
    operations = read_xlsx_operations(file_path)
