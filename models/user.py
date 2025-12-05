class User():
    def __init__(self, name: str, group: str):
        self.__name: str = name
        self.__group: str = group

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) is str and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError("Ошибка")

    @property
    def mail(self):
        return self.__mail

    @mail.setters
    def mail(self, mail: str):
        if type(mail) is str and len(mail) > 5:
            self.__mail = mail
        else:
            raise ValueError('Ошибка')