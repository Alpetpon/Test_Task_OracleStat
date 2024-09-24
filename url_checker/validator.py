"""Модуль для валидации входных данных."""

from typing import List, Tuple
from .utils import is_valid_url

def validate_urls(urls: List[str]) -> Tuple[List[str], List[str]]:
    """
    Валидирует список URL и разделяет их на валидные и невалидные.

    :param urls: Список строк для проверки.
    :return: Кортеж из двух списков: (валидные URL, невалидные строки).
    """
    valid_urls = []
    invalid_urls = []
    for url in urls:
        if is_valid_url(url):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)
    return valid_urls, invalid_urls
