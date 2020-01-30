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

    def stage_two(self):
        print(str(self.unique_id) + " stage two")
