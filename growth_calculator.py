class GrowthCalculator(object):
    def __init__(self):
        """
        Sets default values for the following instance variables:

        Lotka-Volterra equation coefficients:
            self.a - Growing rate of prey when there's no predators
            self.b - Dying rate of prey due to predation
            self.c - Dying rate of predators when there's no prey
            self.d - Reproduction rate of predators per 1 prey eaten

        Other parameters:
            self.dt - Time delta
            self.iterations - Number of iterations to run
            self.predators - Initial predator population count
            self.prey - Initial prey population count
        """

        # Lotka-Volterra equation coefficients
        self.a = 1.0
        self.b = 0.1
        self.c = 1.0
        self.d = 0.075

        # Other parameters
        self.dt = 0.02
        self.iterations = 1000
        self.predators = 5
        self.prey = 10

    def dx(self, x, y):
        """
        Calculates the change in prey population size using the Lotka-Volterra
        equation for prey and the time delta defined in "self.dt"
        """

        # Calculate the rate of population change
        dx_dt = x * (self.a - self.b * y)

        # Calculate the prey population change
        return dx_dt * self.dt

    def dy(self, x, y):
        """
        Calculates the change in predator population size using the
        Lotka-Volterra equation for predators and the time delta defined in
        "self.dt"
        """

        # Calculate the rate of population change
        dy_dt = y * (self.d * x - self.c)

        # Calculate the predator population change
        return dy_dt * self.dt

    def calculate(self):
        """
        Calculates the predator/prey population growth for the given parameters
        (Defined in the __init__ docstring). Returns the following dictionary:

        {'predator': [predator population history as a list],
         'prey': [prey population history as a list]}
        """
        predator_history = []
        prey_history = []

        for i in range(self.iterations):
            xk_1 = self.dx(self.prey, self.predators)
            yk_1 = self.dy(self.prey, self.predators)
            xk_2 = self.dx(self.prey + xk_1, self.predators + yk_1)
            yk_2 = self.dy(self.prey + xk_1, self.predators + yk_1)

            self.prey = self.prey + (xk_1 + xk_2) / 2
            self.predators = self.predators + (yk_1 + yk_2) / 2

            predator_history.append(self.predators)
            prey_history.append(self.prey)

        return {'predator': predator_history, 'prey': prey_history}
