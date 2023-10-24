from app.lib.data_analysis.Calculation import Calculation
from .models import CalculationInputModel, CalculationOutputModel
import pandas as pd


class USProbabilityCalculation(Calculation):
    data_paths = {
        "selected_gender": {
            "path": "",
        },
        "sexual_orientation": {
            "path": "",
        },
        "yearly_income": {
            "path": "",
        },
        "unmarried": {
            "path": "",
        },
        "body_fat": {
            "path": "",
        },
        "age": {
            "path": "",
        },
        "height": {
            "path": "",
        },
    }

    def __init__(self, calculate: CalculationInputModel):
        """
        :raises ValueError:
        :param calculate:
        """
        super().__init__(calculate)

    def execute_calculation(self) -> CalculationOutputModel:
        self._percentage_of_selected_gender()
        self._percentage_of_sexual_orientation()
        self._percentage_of_minimum_yearly_income()
        self._percentage_of_unmarried()
        self._percentage_within_body_fat_range()
        self._percentage_within_age_range()
        self._percentage_within_height_range()

        data = {
            "probability_of_finding_partner": self.execute_calculation()
        }

        return CalculationOutputModel(data=data)

    def _percentage_of_selected_gender(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)

    def _percentage_of_sexual_orientation(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)

    def _percentage_of_minimum_yearly_income(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)

    def _percentage_of_unmarried(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)

    def _percentage_within_body_fat_range(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)

    def _percentage_within_age_range(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)

    def _percentage_within_height_range(self) -> float:
        data_path = self._get_from_data_paths()

        df = pd.read_csv(data_path)
