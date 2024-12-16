from src.coffee_machine_parameters import CoffeePortionTypes, CoffeePortionsCost, PortionIngredients
from src.exceptions import NotEnoughWaterError
from src.portion_maker import PortionMaker


class WaterPortionMaker(PortionMaker):
    def __init__(self, coffee_beans, water, milk):
        super().__init__(coffee_beans, water, milk)
        self.portion_name = CoffeePortionTypes.water
        self.water_cost = CoffeePortionsCost.coffee_portions_cost[self.portion_name]

    def calculate_remain(self) -> None:
        self.water -= self.water_cost[PortionIngredients.water]

    def check_availability(self) -> bool:
        if self.water > self.water_cost[PortionIngredients.water]:
            return True
        raise NotEnoughWaterError
