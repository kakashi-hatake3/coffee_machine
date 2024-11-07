from abc import ABC, abstractmethod

from src.exceptions import NotEnoughCoffeeBeansError, NotEnoughWaterError, NotEnoughMilkError


class AvailabilityChecker(ABC):
    @abstractmethod
    def check_availability(self):
        pass


class PortionExecutor(ABC):
    @abstractmethod
    def make_portion(self):
        pass


class RemainCalculator(ABC):
    @abstractmethod
    def calculate_remain(self):
        pass


class PortionMaker(PortionExecutor, RemainCalculator, AvailabilityChecker):
    def __init__(self, coffee_beans, water, milk):
        self.coffee_beans = coffee_beans
        self.water = water
        self.milk = milk

    def check_availability(self) -> bool:
        pass

    def calculate_remain(self) -> None:
        pass

    def make_portion(self) -> None:
        try:
            self.check_availability()
        except NotEnoughCoffeeBeansError as e:
            print(e)
            exit()
        except NotEnoughWaterError as e:
            print(e)
            exit()
        except NotEnoughMilkError as e:
            print(e)
            exit()
        else:
            self.calculate_remain()
