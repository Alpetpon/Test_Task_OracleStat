"""Главный модуль приложения."""

import asyncio
import argparse
import json
from aiohttp import ClientSession
from url_checker.validator import validate_urls
from url_checker.checker import check_url_methods

async def process_url(session: ClientSession, url: str, timeout: int) -> dict:
    """
    Обрабатывает один URL и возвращает информацию о доступных методах.

    :param session: Сессия aiohttp.
    :param url: URL для обработки.
    :param timeout: Тайм-аут для запросов.
    :return: Словарь с результатами проверки URL.
    """
    methods = await check_url_methods(session, url, timeout)
    return {url: methods}

async def main():
    """
    Главная асинхронная функция приложения.
    """
    parser = argparse.ArgumentParser(
        description='CLI приложение для проверки доступных HTTP методов по заданным ссылкам.'
    )
    parser.add_argument('urls', metavar='URL', nargs='+', help='Список строк для проверки.')
    parser.add_argument('--timeout', type=int, default=10, help='Тайм-аут для запросов (в секундах).')
    parser.add_argument('--output', type=str, help='Путь к файлу для сохранения результатов.')
    args = parser.parse_args()

    valid_urls, invalid_urls = validate_urls(args.urls)

    for invalid_url in invalid_urls:
        print(f'Строка "{invalid_url}" не является ссылкой.')

    result = {}
    async with ClientSession() as session:
        tasks = [process_url(session, url, args.timeout) for url in valid_urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            result.update(response)

    output = json.dumps(result, ensure_ascii=False, indent=4)
    print(output)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)

if __name__ == '__main__':
    asyncio.run(main())
