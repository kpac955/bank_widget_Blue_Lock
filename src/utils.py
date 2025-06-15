import json
import logging
from typing import Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
# Настройка обработчика, форматера
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_data_transactions(file_path: str) -> List[Dict]:
    logger.info(f"Загрузка данных из {file_path}")
    # данная функция открывает файл по-указанному file_path, читает его преобразует в Python объект.
    # после этого мы проверяем, является ли полученный объект списком словарей, если да, то его же ивозвращаем.
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # проверяем что data - список
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} записей")
                return data
            # если data не список - возвращаем пустой список с отловом пары ошибок.
            else:
                logger.warning("Файл не содержит список. Возвращаем []")
                return []

    except FileNotFoundError:
        logger.error(f"Файл по указанному пути не найден: {file_path}")
        return []

    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка в фале {file_path}: {ex}")
        return []
