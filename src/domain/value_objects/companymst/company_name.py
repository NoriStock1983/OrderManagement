class CompanyName:
    """会社名の値オブジェクト"""

    FORBIDDEN_CHARS = ['<', '>', '&', '"', "'"]

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def _validate(self, value: str) -> None:
        if not value:
            raise ValueError("会社名は必須です")

        if not isinstance(value, str):
            raise TypeError("会社名は文字列である必要があります")

        if len(value) > 50:
            raise ValueError("会社名は50文字以内である必要があります")

        for char in self.FORBIDDEN_CHARS:
            if char in value:
                raise ValueError("会社名に使用できない文字が含まれています")

    def __eq__(self, other) -> bool:
        if not isinstance(other, CompanyName):
            return False
        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return self._value
