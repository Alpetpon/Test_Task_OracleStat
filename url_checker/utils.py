"""Вспомогательные функции для приложения."""

import re
from .constants import URL_REGEX

def is_valid_url(url: str) -> bool:
    """
    Проверяет, является ли строка валидным URL.

    :param url: Строка для проверки.
    :return: True, если строка является валидным URL, иначе False.
    """
    return re.match(URL_REGEX, url) is not None
