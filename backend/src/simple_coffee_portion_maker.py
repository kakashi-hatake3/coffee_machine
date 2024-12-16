from src.coffee_machine_parameters import CoffeePortionTypes, CoffeePortionsCost, PortionIngredients
from src.exceptions import NotEnoughWaterError, NotEnoughCoffeeBeansError
from src.portion_maker import PortionMaker


class SimpleCoffeePortionMaker(PortionMaker):
    def __init__(self, coffee_beans, water, milk):
        super().__init__(coffee_beans, water, milk)
        self.portion_name = CoffeePortionTypes.simple_coffee
        self.portion_cost = CoffeePortionsCost.coffee_portions_cost[self.portion_name]

    def calculate_remain(self):
        self.coffee_beans -= self.portion_cost[PortionIngredients.coffee_beans]
        self.water -= self.portion_cost[PortionIngredients.water]

    def check_availability(self):
        if self.coffee_beans > self.portion_cost[PortionIngredients.coffee_beans]:
            if self.water > self.portion_cost[PortionIngredients.water]:
                return True
            else:
                raise NotEnoughWaterError
        raise NotEnoughCoffeeBeansError
