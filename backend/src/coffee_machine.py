from src.americano_maker import AmericanoMaker
from src.cappuccino_maker import CappuccinoMaker
from src.coffee_machine_parameters import CoffeeTypes, CoffeeBrewLimit
from src.coffee_maker import CoffeeMaker
from src.coffee_type_checker import CoffeeTypeChecker
from src.craft_maker import CraftMaker
from src.espresso_maker import EspressoMaker
from src.latte_maker import LatteMaker


class CoffeeMachine:
    def __init__(self, coffee_beans: int, water: int, milk: int):
        self.coffee_beans = coffee_beans
        self.water = water
        self.milk = milk
        self.craft_params = (0, 0, 0)
        self.coffee_maker: CoffeeMaker = CoffeeMaker(self.coffee_beans, self.water, self.milk)
        self.brewed_coffee_count = 0
        self.limit_brewed_coffee_count = CoffeeBrewLimit.max_count

    def make_coffee(self, coffee_type: str) -> str:
        coffee_type_to_coffee_maker_mapper = {
            CoffeeTypes.espresso.value: EspressoMaker(self.coffee_beans, self.water, self.milk),
            CoffeeTypes.americano: AmericanoMaker(self.coffee_beans, self.water, self.milk),
            CoffeeTypes.cappuccino: CappuccinoMaker(self.coffee_beans, self.water, self.milk),
            CoffeeTypes.latte: LatteMaker(self.coffee_beans, self.water, self.milk),
            CoffeeTypes.craft: CraftMaker(self.coffee_beans, self.water, self.milk, self.craft_params),
        }

        if CoffeeTypeChecker(coffee_type).check():
            if self.brewed_coffee_count < self.limit_brewed_coffee_count:
                self.coffee_maker = coffee_type_to_coffee_maker_mapper[coffee_type]
                result = self.coffee_maker.make_coffee()
                self.update_ingredients()
                self.brewed_coffee_count += 1
                return result
            else:
                return 'Почистите кофе-машину!'
        else:
            return 'Такого кофе нет в меню'

    def update_ingredients(self):
        self.coffee_beans = self.coffee_maker.coffee_beans
        self.water = self.coffee_maker.water
        self.milk = self.coffee_maker.milk

    def get_left_count_of_coffee(self) -> str:
        return f'Осталось {self.limit_brewed_coffee_count - self.brewed_coffee_count} чашек до загрязнения кофе-машины'

    def get_left_ingredients(self) -> str:
        return f'Зерна: {self.coffee_beans}гр, Вода: {self.water}мл, Молоко: {self.milk}мл'
    
    def clean_machine(self) -> str:
        if self.brewed_coffee_count > 0:
            self.brewed_coffee_count = 0
            return "Кофе-машина успешно очищена!"
        return "Кофе-машина уже чистая!"
