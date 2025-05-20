import json
from typing import Dict, List


def load_data_transactions(file_path: str) -> List[Dict]:
    # данная функция открывает файл по-указанному file_path, читает его преобразует в Python объект.
    # после этого мы проверяем, является ли полученный объект списком словарей, если да, то его же ивозвращаем.
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # проверяем что data - список
            if isinstance(data, list):
                return data
            # если data не список - возвращаем пустой список с отловом пары ошибок.
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
