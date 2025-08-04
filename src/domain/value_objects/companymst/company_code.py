import re


class CompanyCode:
    """会社コードの値オブジェクト"""

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def _validate(self, value: str) -> None:
        if not value:
            raise ValueError("会社コードは必須です")

        if not isinstance(value, str):
            raise TypeError("会社コードは文字列である必要があります")

        if len(value) > 3:
            raise ValueError("会社コードは3文字以内である必要があります")

        if not re.match(r"^\d{1,3}$", value):
            raise ValueError("会社コードは半角数字のみ使用できます")

    def __eq__(self, other) -> bool:
        if not isinstance(other, CompanyCode):
            return False
        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return self._value
