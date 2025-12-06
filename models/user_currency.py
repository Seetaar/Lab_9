class UserCurrency:
    def __init__(self, id: int, user_id: int, currency_id: str):
        self._id = None
        self._user_id = None
        self._currency_id = None
        self.id = id
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("ID - целое число")
        if value <= 0:
            raise ValueError("Введите ID")
        self._id = value
        self._user_id = value
        self._currency_id = value.strip()

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'currency_id': self.currency_id
        }
