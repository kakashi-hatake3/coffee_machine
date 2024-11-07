from src.coffee_machine_parameters import CoffeePortionTypes, CoffeePortionsCost, PortionIngredients
from src.exceptions import NotEnoughWaterError, NotEnoughMilkError
from src.portion_maker import PortionMaker


class MilkPortionMaker(PortionMaker):
    def __init__(self, coffee_beans, water, milk):
        super().__init__(coffee_beans, water, milk)
        self.portion_name = CoffeePortionTypes.milk
        self.milk_cost = CoffeePortionsCost.coffee_portions_cost[self.portion_name]

    def calculate_remain(self) -> None:
        self.water -= self.milk_cost[PortionIngredients.water]
        self.milk -= self.milk_cost[PortionIngredients.milk]

    def check_availability(self) -> bool:
        if self.milk > self.milk_cost[PortionIngredients.milk]:
            if self.water > self.milk_cost[PortionIngredients.water]:
                return True
            else:
                raise NotEnoughWaterError
        raise NotEnoughMilkError
