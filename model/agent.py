from mesa import Agent


class HometimeAgent(Agent):
    """Agent in simulation"""
    def __init__(self, unique_id, model, weather_weight, likelihood_to_eat_out,
                 likelihood_to_eat_out_weight, restaurant_likability,
                 restaurant_likability_weight, previous_visits,
                 previous_visits_weight, home_x_pos, home_y_pos,
                 distance_weight):
        """Make a new agent"""
        super().__init__(unique_id, model)

        self.weather_weight = weather_weight
        self.likelihood_to_eat_out = likelihood_to_eat_out
        self.likelihood_to_eat_out_weight = likelihood_to_eat_out_weight
        self.restaurant_likability = restaurant_likability
        self.restaurant_likability_weight = restaurant_likability_weight
        self.previous_visits = previous_visits
        self.previous_visits_weight = previous_visits_weight
        self.home_x_pos = home_x_pos
        self.home_y_pos = home_y_pos
        self.distance_weight = distance_weight

    def step(self):
        """This is called on every time step"""
        pass

    def stage_one(self):
        print(str(self.unique_id) + " stage one")

        # utility = self.calculate_utility()
        # print(str(self.unique_id) + "'s utility is " + str(utility))

    def stage_two(self):
        print(str(self.unique_id) + " stage two")

    def calculate_utility(self, restaurant_name):
        utility = 0
        if self.model.good_weather:
            utility += 0 * self.weather_weight
        else:
            utility += -1 * self.weather_weight

        utility += (self.likelihood_to_eat_out *
                    self.likelihood_to_eat_out_weight)
        utility += (self.restaurant_likability[restaurant_name] *
                    self.restaurant_likability_weight)

        utility += (self.previous_visits[restaurant_name] *
                    self.previous_visits_weight)

        return utility
