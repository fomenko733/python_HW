# string_utils.py

class StringUtils:
    def capitalize(self, string: str) -> str:
        """Преобразует первый символ строки в заглавный, остальные — в строчные."""
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        return string.capitalize()

    def trim(self, string: str) -> str:
        """Удаляет пробелы в начале строки."""
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        return string.lstrip()

    def to_list(self, string: str, delimiter=",") -> list:
        """Преобразует строку в список по разделителю."""
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        if string == "":
            return []
        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:
        """Проверяет, содержит ли строка символ."""
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("Both arguments must be strings")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """Удаляет все вхождения символа из строки."""
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("Both arguments must be strings")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")
        return string.replace(symbol, "")

    def starts_with(self, string: str, prefix: str) -> bool:
        """Проверяет, начинается ли строка с указанного префикса."""
        if not isinstance(string, str) or not isinstance(prefix, str):
            raise TypeError("Both arguments must be strings")
        return string.startswith(prefix)

    def end_with(self, string: str, suffix: str) -> bool:
        """Проверяет, заканчивается ли строка указанным суффиксом."""
        if not isinstance(string, str) or not isinstance(suffix, str):
            raise TypeError("Both arguments must be strings")
        return string.endswith(suffix)

    def is_empty(self, string: str) -> bool:
        """Проверяет, пустая ли строка или состоит только из пробелов."""
        if not isinstance(string, str):
            raise TypeError("Input must be a string")
        return string.strip() == ""

    def list_to_string(self, lst: list, joiner=", ") -> str:
        """Преобразует список в строку с указанным разделителем."""
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        return joiner.join(str(item) for item in lst)