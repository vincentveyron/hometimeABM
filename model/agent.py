from mesa import Agent


class HometimeAgent(Agent):
    """Agent in simulation"""
    def __init__(self, unique_id, model, weather_weight):
        """Make a new agent"""
        super().__init__(unique_id, model)

        self.weather_weight = weather_weight

    def step(self):
        """This is called on every time step"""
        pass

    def stage_one(self):
        print(str(self.unique_id) + " stage one")
        utility = self.calculate_utility()
        print(str(self.unique_id) + "'s utility is " + str(utility))

    def stage_two(self):
        print(str(self.unique_id) + " stage two")

    def calculate_utility(self):
        utility = 0
        if self.model.good_weather:
            utility += 0 * self.weather_weight
        else:
            utility += -1 * self.weather_weight
        return utility
