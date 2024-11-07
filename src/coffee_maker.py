from src.coffee_machine_parameters import CoffeeCostInPortions, CoffeePortionTypes
from src.milk_portion_maker import MilkPortionMaker
from src.portion_maker import PortionMaker
from src.simple_coffee_portion_maker import SimpleCoffeePortionMaker
from src.water_portion_maker import WaterPortionMaker


class CoffeeMaker:
    def __init__(self, coffee_beans, water, milk):
        self.coffee_beans = coffee_beans
        self.water = water
        self.milk = milk

        self.portion_maker: PortionMaker | None = None

        self.coffee_cost_in_portions = CoffeeCostInPortions.coffee_cost_in_portions

        self.coffee_type = ''
        self.coffee_cost = {}

        self.portion_name_to_portion_maker_mapper = {
            CoffeePortionTypes.simple_coffee: SimpleCoffeePortionMaker,
            CoffeePortionTypes.water: WaterPortionMaker,
            CoffeePortionTypes.milk: MilkPortionMaker,
        }

    def init_portion_maker(self, portion_maker_class) -> None:
        self.portion_maker = portion_maker_class(
            self.coffee_beans,
            self.water,
            self.milk
        )

    def update_ingredients(self) -> None:
        self.coffee_beans = self.portion_maker.coffee_beans
        self.water = self.portion_maker.water
        self.milk = self.portion_maker.milk

    def make_coffee(self) -> str:
        for portion_name, portion_count in self.coffee_cost.items():
            for i in range(portion_count):
                self.init_portion_maker(self.portion_name_to_portion_maker_mapper[portion_name])
                self.portion_maker.make_portion()
                self.update_ingredients()
        return f'Ваш {self.coffee_type} готов!'
