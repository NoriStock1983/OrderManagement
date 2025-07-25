class UpdateCounter:
    """更新カウンタの値オブジェクト"""

    def __init__(self, value: int = 0):
        self._validate(value)
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def _validate(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("更新カウンタは整数である必要があります")

        if value < 0:
            raise ValueError("更新カウンタは0以上である必要があります")

    def increment(self) -> 'UpdateCounter':
        """更新カウンタをインクリメントした新しいインスタンスを返す"""
        return UpdateCounter(self._value + 1)

    def __eq__(self, other) -> bool:
        if not isinstance(other, UpdateCounter):
            return False
        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return str(self._value)
