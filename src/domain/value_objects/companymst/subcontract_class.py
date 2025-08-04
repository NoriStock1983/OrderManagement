class SubcontractClass:
    """外注区分の値オブジェクト"""

    SELF_COMPANY = "00"  # 自社
    SUBCONTRACT = "01"  # 外注
    PARTNER = "02"  # 協力会社

    ALLOWED_VALUES = [SELF_COMPANY, SUBCONTRACT, PARTNER]

    def __init__(self, value: str):
        self._validate(value)
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def _validate(self, value: str) -> None:
        if not value:
            raise ValueError("外注区分は必須です")

        if not isinstance(value, str):
            raise TypeError("外注区分は文字列である必要があります")

        if value not in self.ALLOWED_VALUES:
            raise ValueError("外注区分は00, 01, 02のいずれかである必要があります")

    def is_self_company(self) -> bool:
        """自社かどうかを判定"""
        return self._value == self.SELF_COMPANY

    def is_subcontract(self) -> bool:
        """外注かどうかを判定"""
        return self._value == self.SUBCONTRACT

    def is_partner(self) -> bool:
        """協力会社かどうかを判定"""
        return self._value == self.PARTNER

    def __eq__(self, other) -> bool:
        if not isinstance(other, SubcontractClass):
            return False
        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return self._value
