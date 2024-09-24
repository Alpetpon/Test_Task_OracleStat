"""Модуль для проверки доступных HTTP методов по URL."""

import asyncio
from typing import Dict
from .constants import HTTP_METHODS
import logging
from aiohttp import ClientSession, ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def check_method(session: ClientSession, url: str, method: str, timeout: int) -> tuple:
    """
    Проверяет доступность метода для заданного URL.

    :param session: Сессия aiohttp.
    :param url: URL для проверки.
    :param method: HTTP метод для проверки.
    :param timeout: Тайм-аут для запроса.
    :return: Кортеж (метод, статус код или None).
    """
    try:
        async with session.request(method, url, allow_redirects=False, timeout=timeout) as response:
            logger.info(f"Method: {method}, URL: {url}, Status: {response.status}")
            if response.status != 405:
                return method, response.status
            else:
                logger.info(f"Method {method} on {url} returned status 405")
    except ClientError as e:
        logger.error(f"ClientError for {method} {url}: {e}")
    except asyncio.TimeoutError as e:
        logger.error(f"TimeoutError for {method} {url}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error for {method} {url}: {e}")
    return method, None

async def check_url_methods(session: ClientSession, url: str, timeout: int) -> Dict[str, int]:
    """
    Проверяет все доступные HTTP методы для заданного URL.

    :param session: Сессия aiohttp.
    :param url: URL для проверки.
    :param timeout: Тайм-аут для запросов.
    :return: Словарь доступных методов и их статус кодов.
    """
    tasks = [check_method(session, url, method, timeout) for method in HTTP_METHODS]
    results = await asyncio.gather(*tasks)
    available_methods = {method: status for method, status in results if status is not None}
    logger.info(f"Available methods for {url}: {available_methods}")
    return available_methods
