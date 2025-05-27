import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Настройка обработчика и форматера
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
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
