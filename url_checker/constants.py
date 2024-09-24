"""Модуль с константами для приложения."""

HTTP_METHODS = [
    'GET', 'POST', 'PUT', 'DELETE', 'HEAD',
    'OPTIONS', 'PATCH', 'TRACE', 'CONNECT'
]

URL_REGEX = r'^(?:http|ftp)s?://\S+$'
