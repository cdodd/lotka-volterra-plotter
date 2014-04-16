# Local application modules
from growth_calculator import GrowthCalculator


class TestGrowthCalculator:
    def setup(self):
        self.growth_calculator = GrowthCalculator()

    def teardown(self):
        del(self.growth_calculator)

    def test_growth_calculator_1(self):
        self.growth_calculator.a = 0.02
        self.growth_calculator.b = 0.1
        self.growth_calculator.c = 1.0
        self.growth_calculator.d = 0.075
        self.growth_calculator.predators = 5
        self.growth_calculator.prey = 10
        self.growth_calculator.iterations = 5
        self.growth_calculator.dt = 0.02

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
        actual_results = self.growth_calculator.calculate()
        assert(actual_results == expected_results)

    def test_growth_calculator_2(self):
        self.growth_calculator.a = 0.04
        self.growth_calculator.b = 0.1
        self.growth_calculator.c = 1.0
        self.growth_calculator.d = 0.073
        self.growth_calculator.predators = 3
        self.growth_calculator.prey = 20
        self.growth_calculator.iterations = 7
        self.growth_calculator.dt = 0.01

        # Define the expected results
        expected_results = {
            'prey': [
                19.9479299588,
                19.895721936011856,
                19.8433787738455,
                19.790903335727396,
                19.738298505684906,
                19.685567187722064,
                19.632712305186992,
            ],
            'predator': [
                3.013774538076,
                3.0274970884979107,
                3.0411660643883405,
                3.0547798800787245,
                3.068336951550548,
                3.0818356968782594,
                3.095274536673641,
            ],
        }

        # Calculate the population growths and compare to the expected results
        actual_results = self.growth_calculator.calculate()
        assert(actual_results == expected_results)
