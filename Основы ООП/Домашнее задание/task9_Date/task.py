from typing import Union


class Date_:
    def __init__(self, dd: Union[int], mm: Union[int],  yyyy: Union[int]):
        self.dd = self.__check_dd(dd)
        self.mm = self.__check_mm(mm)
        self.yyyy = self.__check_yyyy(yyyy)



    @staticmethod
    def __check_dd(value):
        if not isinstance(value, int):
            raise TypeError
        if not 0 < value < 32:
            raise ValueError
        return value

    @staticmethod
    def __check_mm(value):
        if not isinstance(value, int):
            raise TypeError
        if not 0 < value < 13:
            raise ValueError
        return value

    @staticmethod
    def __check_yyyy(value):
        if not isinstance(value, int):
            raise TypeError
        if not 1900 < value < 2100:
            raise ValueError
        return value


    def __repr__(self) -> str:
        return f"Data({self.dd}.{self.mm}.{self.yyyy})"

    def __str__(self) -> str:
        return f"{self.dd}/{self.mm}/{self.yyyy}"


if __name__ == "__name__":
    glass1 = Date_(222, 110, 1901)
    print(glass1.__repr__())  # TDO инициализировать два объекта типа Glass
    print("w")

