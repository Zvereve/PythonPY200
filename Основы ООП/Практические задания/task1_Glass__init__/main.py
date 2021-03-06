from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.occupied_volume = self.__check_occupied_volume(occupied_volume)
        self.__check_over()


    @staticmethod
    def __check_capacity_volume(value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        return value


    def __check_over(self):
        if self.capacity_volume < self.occupied_volume:
            raise OverflowError('Стакан не резиновый')


if __name__ == "__main__":
    glass1 = Glass(200, 100)
    glass2 = Glass(200, 50)  # TDO инициализировать два объекта типа Glass


