from mesa import Model
from mesa.space import ContinuousSpace
from mesa.time import StagedActivation
from model.agent import HometimeAgent


class HometimeModel(Model):
    """This is a model that allows simulation of secondary school children to
    commute home from school and/or stop off at restaurants"""
    def __init__(self, N=100, width=100, height=100):
        """Makes the new model

        Arguments
        =========
        - N - number of agents, default: 100
        - width - the width of grid, default: 100
        - height - height of grid, default: 100
        """
        self.num_agents = N
        self.grid = ContinuousSpace(width, height, False)
        model_stages = ["stage_one", "stage_two"]
        self.schedule = StagedActivation(self, model_stages, True)

        for i in range(0, self.num_agents):
            agent = HometimeAgent(i, self)
            self.schedule.add(agent)

        self.running = True

    def step(self):
        self.schedule.step()
