from mesa import Model
from mesa.time import StagedActivation
from model.agent import HometimeAgent
from model import config
from random import random
from database.database_helper import get_all_restaurants
import numpy as np


class HometimeModel(Model):
    """This is a model that allows simulation of secondary school children to
    commute home from school and/or stop off at restaurants"""
    def __init__(self, db_connection, N=100, width=100, height=100,
                 school_x_pos=50, school_y_pos=50):
        """Makes the new model

        Arguments
        =========
        - N - number of agents, default: 100
        - width - the width of grid, default: 100
        - height - height of grid, default: 100
        """
        self.num_agents = N
        model_stages = ["stage_one", "stage_two"]
        self.schedule = StagedActivation(self, model_stages, True)

        self.restaurants = get_all_restaurants(db_connection)
        self.school_x_pos = school_x_pos
        self.school_y_pos = school_y_pos

        # this is true when the weather is good, false otherwise
        self.good_weather = True

        for i in range(0, self.num_agents):
            id = i
            model = self

            # Generate weather weight as Normal distribution
            # Mean - 0.5. SD - 0.25
            weather_weight = np.random.normal(0.5, 0.25)

            # Generate likelihood to eat out as Normal distribution
            # Mean - 0.5. SD - 0.25
            likelihood_to_eat_out = np.random.normal(0.5, 0.25)
            likelihood_to_eat_out_weight = 1.0

            # Randomizes likability for each restaurant
            restaurant_likability = {}
            for restaurant in self.restaurants:
                restaurant_name = restaurant[0]
                restaurant_likability[restaurant_name] = np.random.normal(
                    0.5, 0.25
                )

            restaurant_likability_weight = 1.0

            # Previous visit values
            previous_visits = {}
            for restaurant in self.restaurants:
                restaurant_name = restaurant[0]
                previous_visits[restaurant_name] = 0

            previous_visit_weight = 1.0

            home_x_pos = np.random.uniform(0, width)
            home_y_pos = np.random.uniform(0, height)

            distance_weight = np.random.normal(-0.5, 0.25)

            agent = HometimeAgent(
                id,
                model,
                weather_weight,
                likelihood_to_eat_out,
                likelihood_to_eat_out_weight,
                restaurant_likability,
                restaurant_likability_weight,
                previous_visits,
                previous_visit_weight,
                home_x_pos,
                home_y_pos,
                distance_weight
            )
            self.schedule.add(agent)

        self.running = True

    def step(self):
        # change the weather
        if random() < config.percentage_bad_weather:
            self.good_weather = False
        else:
            self.good_weather = True

        self.schedule.step()
