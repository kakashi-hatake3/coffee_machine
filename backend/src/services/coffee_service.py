from src.coffee_machine import CoffeeMachine

class CoffeeMachineService:
    def __init__(self, coffee_beans: int, water: int, milk: int):
        self.coffee_machine = CoffeeMachine(coffee_beans, water, milk)

    def make_coffee(self, coffee_type: str) -> str:
        return self.coffee_machine.make_coffee(coffee_type)

    def set_craft_params(self, coffee: int, water: int, milk: int):
        self.coffee_machine.craft_params = (coffee, water, milk)

    def get_coffee_beans(self) -> int:
        return self.coffee_machine.coffee_beans

    def get_water(self) -> int:
        return self.coffee_machine.water

    def get_milk(self) -> int:
        return self.coffee_machine.milk

    def get_brewed_count(self) -> int:
        return self.coffee_machine.brewed_coffee_count

    def get_remaining_brews(self) -> int:
        return self.coffee_machine.limit_brewed_coffee_count - self.coffee_machine.brewed_coffee_count
    
    def clean_machine(self) -> str:
        return self.coffee_machine.clean_machine()
