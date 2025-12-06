class Currency:
    def __init__(self, id: str, num_code: str, char_code: str,
                 name: str, value: float, nominal: int):
        self._id = None
        self._num_code = None
        self._char_code = None
        self._name = None
        self._value = None
        self._nominal = None
        self.id = id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("ID must be a string")
        if not value.strip():
            raise ValueError("ID cannot be empty")
        self._id = value.strip()

    @property
    def num_code(self) -> str:
        return self._num_code

    @num_code.setter
    def num_code(self, value: str):
        if not isinstance(value, str):
            raise TypeError("NumCode must be a string")
        if not value.strip():
            raise ValueError("NumCode cannot be empty")
        self._num_code = value.strip()

    @property
    def char_code(self) -> str:
        return self._char_code

    @char_code.setter
    def char_code(self, value: str):
        if not isinstance(value, str):
            raise TypeError("CharCode must be a string")
        if not value.strip():
            raise ValueError("CharCode cannot be empty")
        self._char_code = value.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value <= 0:
            raise ValueError("Value must be positive")
        self._value = float(value)

    @property
    def nominal(self) -> int:
        return self._nominal

    @nominal.setter
    def nominal(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Nominal must be an integer")
        if value <= 0:
            raise ValueError("Nominal must be positive")
        self._nominal = value

    def unit_value(self) -> float:
        """Возвращает стоимость за 1 единицу валюты"""
        return self.value / self.nominal

    def to_dict(self):
        return {
            'id': self.id,
            'num_code': self.num_code,
            'char_code': self.char_code,
            'name': self.name,
            'value': self.value,
            'nominal': self.nominal,
            'unit_value': self.unit_value()
        }