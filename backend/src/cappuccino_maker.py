from src.coffee_machine_parameters import CoffeeTypes
from src.coffee_maker import CoffeeMaker


class CappuccinoMaker(CoffeeMaker):
    def __init__(self, coffee_beans, water, milk):
        super().__init__(coffee_beans, water, milk)
        self.coffee_type = CoffeeTypes.cappuccino
        self.coffee_cost = self.coffee_cost_in_portions[self.coffee_type]
