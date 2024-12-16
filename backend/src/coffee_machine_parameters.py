from enum import StrEnum


class CoffeeTypes(StrEnum):
    espresso = 'espresso'
    americano = 'americano'
    cappuccino = 'cappuccino'
    latte = 'latte'
    craft = 'craft'


class CoffeeTypesList:
    coffee_types_list = [
        CoffeeTypes.espresso,
        CoffeeTypes.americano,
        CoffeeTypes.cappuccino,
        CoffeeTypes.latte,
        CoffeeTypes.craft,
    ]


class CoffeePortionTypes(StrEnum):
    simple_coffee = 'simple_coffee'
    water = 'water'
    milk = 'milk'


class CoffeeCostInPortions:
    coffee_cost_in_portions = {
        CoffeeTypes.espresso: {
            CoffeePortionTypes.simple_coffee: 1,
            CoffeePortionTypes.water: 0,
            CoffeePortionTypes.milk: 0,
        },
        CoffeeTypes.americano: {
            CoffeePortionTypes.simple_coffee: 1,
            CoffeePortionTypes.water: 2,
            CoffeePortionTypes.milk: 0,
        },
        CoffeeTypes.cappuccino: {
            CoffeePortionTypes.simple_coffee: 1,
            CoffeePortionTypes.water: 0,
            CoffeePortionTypes.milk: 4,
        },
        CoffeeTypes.latte: {
            CoffeePortionTypes.simple_coffee: 1,
            CoffeePortionTypes.water: 0,
            CoffeePortionTypes.milk: 6,
        },
    }


class PortionIngredients(StrEnum):
    coffee_beans = 'coffee_beans'
    water = 'water'
    milk = 'milk'


class CoffeePortionsCost:
    coffee_portions_cost = {
        CoffeePortionTypes.simple_coffee: {
            PortionIngredients.coffee_beans: 15,
            PortionIngredients.water: 45,
            PortionIngredients.milk: 0,
        },
        CoffeePortionTypes.water: {
            PortionIngredients.coffee_beans: 0,
            PortionIngredients.water: 30,
            PortionIngredients.milk: 0,
        },
        CoffeePortionTypes.milk: {
            PortionIngredients.coffee_beans: 0,
            PortionIngredients.water: 1.5,
            PortionIngredients.milk: 30,
        },
    }


class CoffeeBrewLimit:
    max_count = 3
