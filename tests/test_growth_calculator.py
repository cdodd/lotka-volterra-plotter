# Local application modules
from growth_calculator import GrowthCalculator


class TestGrowthCalculator:
    def setup(self):
        self.growth_calculator = GrowthCalculator()

    def teardown(self):
        del(self.growth_calculator)

    def test_growth_calculator_1(self):
        # Create a GrowthCalculator object and populate with parameters
        growth = GrowthCalculator()
        growth.a = 0.02
        growth.b = 0.1
        growth.c = 1.0
        growth.d = 0.075
        growth.predators = 5
        growth.prey = 10
        growth.iterations = 5
        growth.dt = 0.02

        # Define the expected results
        expected_results = {
            'prey': [
                9.9047084,
                9.810826891605023,
                9.718343504557055,
                9.627245889460662,
                9.537521345656497,
            ],
            'predator': [
                4.9747043,
                4.94883441612808,
                4.922411023677906,
                4.895454666361016,
                4.867985738110833,
            ],
        }

        # Calculate the population growths and compare to the expected results
        actual_results = growth.calculate()
        assert(actual_results == expected_results)
