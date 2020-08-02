"""
3/21/2020

Purpose:
    Container for the unique latitude and longitude

"""
from typing import Tuple


class LatitudeLongitudeContainer:
    def __init__(self, tuple_lat_long: Tuple[int, int]):
        self.tuple_lat_long = tuple_lat_long

        # Amount of reported incidents
        self.count_infected = 0  # type: int

        self.country = ""  # type: str

        self.province = ""  # type: str

        self.city = ""  # type: str

        self.set_date_confirmation = set()  # type: set

    def __str__(self):
        string = "{:<40} {}".format(str(self.tuple_lat_long), self.count_infected)

        return string

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.tuple_lat_long)

    def __lt__(self, other):
        if isinstance(other, LatitudeLongitudeContainer):
            return self.count_infected < other.count_infected

        if isinstance(other, int):
            return self.count_infected < other

    def __le__(self, other):
        if isinstance(other, LatitudeLongitudeContainer):
            return self.count_infected <= other.count_infected

        if isinstance(other, int):
            return self.count_infected <= other

    def __eq__(self, other):
        if isinstance(other, LatitudeLongitudeContainer):
            return self.__hash__() == other.__hash__()
        if isinstance(other, int):
            return self.__hash__() == other

    def __ne__(self, other):
        # if isinstance(other, LatitudeLongitudeContainer):
        #     return self.__hash__() == other.__hash__()
        # if isinstance(other, int):
        #     return self.__hash__() == other
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, LatitudeLongitudeContainer):
            return self.count_infected > other.count_infected

        if isinstance(other, int):
            return self.count_infected > other

    def __ge__(self, other):
        if isinstance(other, LatitudeLongitudeContainer):
            return self.count_infected >= other.count_infected

        if isinstance(other, int):
            return self.count_infected >= other
