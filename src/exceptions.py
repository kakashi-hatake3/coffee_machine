class NotEnoughCoffeeBeansError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Мало зерен кофе!'


class NotEnoughWaterError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Мало воды!'


class NotEnoughMilkError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Мало молока!'


class CoffeeLimitError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Очистите кофе-машину!'
