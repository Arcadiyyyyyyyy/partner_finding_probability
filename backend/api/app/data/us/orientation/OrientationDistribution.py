from enum import Enum


class Orientation(Enum):
    straight: float
    gay: float
    lesbian: float
    other: float


class OrientationDistribution:
    DISTRIBUTION_DATA = {
        Orientation.straight.name: 0.5,
        Orientation.gay.name: 0.4,
        Orientation.lesbian.name: 0.1,
        Orientation.other.name: 0.1,
    }

    def get_distribution_by_orientation(self, gender_to_search_for: Orientation):
        return self.DISTRIBUTION_DATA.get(gender_to_search_for)
