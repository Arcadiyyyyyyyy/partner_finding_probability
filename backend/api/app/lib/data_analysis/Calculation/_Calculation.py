from pydantic import BaseModel

from app.lib.models import BaseCalculationInputModel


class Calculation:
    input_requirements: BaseCalculationInputModel = None
    probabilities: set[float] = set({})
    data_paths: dict[str, dict[str, str]]

    def __init__(self, calculate: BaseCalculationInputModel):
        """
        Region calculation classes factory

        :raises ValueError:
        """
        self.input_requirements = calculate
        self._validate_input()

    def execute_calculation(self) -> BaseModel:
        raise NotImplementedError

    def _validate_input(self):
        pass
        # raise ValueError("Validation failed because of incompatible input")

    def _calculate_probability(self):
        return map(lambda x, y: x * y, self.probabilities)

    def _get_from_data_paths(self, path_in_dict: str, what_to_get: str = "path"):
        data_path = self.data_paths.get(path_in_dict, {}).get(what_to_get, "")
        if data_path == "":
            raise ValueError("Wrong path of the data for calculations")
        return data_path

    def _percentage_of_selected_gender(self) -> float:
        raise NotImplementedError

    def _percentage_of_sexual_orientation(self) -> float:
        raise NotImplementedError

    def _percentage_of_minimum_yearly_income(self) -> float:
        raise NotImplementedError

    def _percentage_of_unmarried(self) -> float:
        raise NotImplementedError

    def _percentage_within_body_fat_range(self) -> float:
        raise NotImplementedError

    def _percentage_within_age_range(self) -> float:
        raise NotImplementedError

    def _percentage_within_height_range(self) -> float:
        raise NotImplementedError
