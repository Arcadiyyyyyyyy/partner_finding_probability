from enum import Enum


class Genders(Enum):
    males: float
    females: float
    other: float


class GenderDistribution:
    DISTRIBUTION_DATA = {
        Genders.males.name: 0.5,
        Genders.females.name: 0.4,
        Genders.other.name: 0.1,
    }

    def get_distribution_by_gender(self, gender_to_search_for: Genders):
        return self.DISTRIBUTION_DATA.get(gender_to_search_for)
