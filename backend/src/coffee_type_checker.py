from src.coffee_machine_parameters import CoffeeTypesList


class CoffeeTypeChecker:
    def __init__(self, coffee_type: str):
        self.coffee_type = coffee_type

    def check(self):
        if self.coffee_type in CoffeeTypesList.coffee_types_list:
            return True
        return False