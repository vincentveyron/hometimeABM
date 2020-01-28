from mesa import Agent


class HometimeAgent(Agent):
    """Agent in simulation"""
    def __init__(self, unique_id, model):
        """Make a new agent"""
        super().__init__(unique_id, model)

    def step(self):
        """This is called on every time step"""
        pass
