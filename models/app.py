from .author import Author


class App:
    def __init__(self, name: str, version: str, author: Author):
        self.__name = None
        self.__version = None
        self.__author = None
        self.__name = name
        self.__version = version
        self.__author = author

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value.strip()

    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Version must be a string")
        if not value.strip():
            raise ValueError("Version cannot be empty")
        self.__version = value.strip()

    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, value: Author):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author class")
        self.__author = value

    def to_dict(self):
        return {
            'name': self.name,
            'version': self.version,
            'author': self.author.to_dict()
        }