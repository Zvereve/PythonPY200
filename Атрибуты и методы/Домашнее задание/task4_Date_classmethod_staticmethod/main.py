class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)
        print(self.day, self.month, self.year)

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        if self.year % 4 == 0:
            return 1
        else:
            return 0


    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        DAY_OF_MONTH = (
            (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
            (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
        )
        mon = DAY_OF_MONTH[self.is_leap_year(year)]
        return mon[month - 1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not 999 < year < 10000:
            raise IndexError
        if not 1 <= month <= 12:
            raise IndexError
        if not 0 < day <= self.get_max_day(month, year):
            raise IndexError

if __name__ == "__main__":
    # Write your solution here
    Date(29, 2, 2004)
