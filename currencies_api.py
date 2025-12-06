import unittest
import requests
import sys
import io
import functools


def logger(func=None, *, handle=sys.stdout):
    """
    декоратор logger

    Args:
        func: Декорируемая функция
        handle: объект логирования с методом
    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            handle.write("Вызов функции")
            try:
                result = f(*args, **kwargs)

                handle.write(f"Результат: {result}\n")

                return result

            except Exception as e:
                handle.write("Ошибка")
                raise ValueError

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)


stream = io.StringIO()


@logger(handle=sys.stdout)
def get_currencies(currency_codes: list, url: str = "https://www.cbr-xml-daily.ru/daily_json.js",
                   handle=sys.stdout) -> dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
    """
    try:

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        currencies = {}

        if "Valute" in data:
            for code in currency_codes:
                if code in data["Valute"]:
                    currencies[code] = data["Valute"][code]["Value"]
                else:
                    currencies[code] = f"Код валюты '{code}' не найден."
        return currencies

    except requests.exceptions.RequestException as e:
        handle.write(f"Ошибка при запросе к API: {e}")
        raise ValueError


if __name__ == "__main__":
    get_currencies()
