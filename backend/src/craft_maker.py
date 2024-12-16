from src.coffee_machine_parameters import CoffeeTypes, CoffeePortionTypes
from src.coffee_maker import CoffeeMaker


class CraftMaker(CoffeeMaker):
    def __init__(self, coffee_beans, water, milk, craft_params):
        super().__init__(coffee_beans, water, milk)
        self.coffee_type = CoffeeTypes.craft
        self.coffee_cost = {
            CoffeePortionTypes.simple_coffee: craft_params[0],
            CoffeePortionTypes.water: craft_params[1],
            CoffeePortionTypes.milk: craft_params[2],
        }
