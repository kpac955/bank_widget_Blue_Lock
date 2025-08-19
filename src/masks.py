import os
import logging
from typing import Union

# Создаем папку logs в корне проекта если её нет
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Настройка обработчика и форматера
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Прописываем функцию маскировки номера банковской карты клиента"""
    logger.debug(f"Начало маскировки карты {card_number}")

    try:
        result = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.info(f"Успешная маскировка карты: {result}")
        return result
    except Exception as ex:
        logger.error(f"Ошибка маскировки карты: {card_number}: {ex}", exc_info=True)
        return "Ошибка маскировки"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Прописываем функцию маскировки номера счета клиента"""
    logger.debug(f"Начало маскировки счета: {account_number}")

    try:
        result = f"** {account_number[-4:]}"
        logger.info(f"Успешная маскировка счета: {result}")
        return result
    except Exception as ex:
        logger.error(f"Ошибка маскировки счета: {account_number}: {ex}", exc_info=True)
        return "Ошибка маскировки"
