import csv
import logging
import os
from datetime import datetime
from typing import List, Optional, TypedDict

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


def read_csv_operations(file_path: str) -> List[Operation]:

    operations = []
    logging.info(f"Идет чтение файла: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            line_number = 1

            for row in reader:
                line_number += 1

                if not any(row.values()):
                    logging.warning(f"Пропущена пустая строка {line_number}")
                    continue

                try:
                    operation = {
                        "id": int(row["id"]),
                        "state": row["state"],
                        "date": datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%SZ"),
                        "amount": float(row["amount"]),
                        "currency_name": row["currency_name"],
                        "currency_code": row["currency_code"],
                        "from_account": row["from"] or None,
                        "to_account": row["to"],
                        "description": row["description"],
                    }
                    operations.append(operation)
                    logging.info(f"Операция с id {operation['id']} прочитана успешно строка {line_number})")
                except (ValueError, KeyError) as e:
                    logging.warning(f"Ошибка обработки строки {line_number}: {str(e)}. Данные: {row}")

    except FileNotFoundError:
        logging.error(f"Файл {file_path} не найден")
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except Exception as e:
        logging.error(f"Ошибка при чтении файла {str(e)}")
        raise Exception(f"Ошибка при чтении файла:{str(e)}")

    logging.info(f"Работа с файлом завершена. Всего прочитано: {len(operations)}")
    return operations


if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "transactions.csv")
    operations = read_csv_operations(file_path)
