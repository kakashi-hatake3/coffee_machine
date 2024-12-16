# import os
# from time import sleep

# from src.coffee_machine import CoffeeMachine
# from src.coffee_machine_parameters import CoffeeTypesList
# from src.menu import Menu


# def main():
#     coffee_beans = int(input('Введите кол-во зерен в граммах: '))
#     water = int(input('Введите кол-во воды в миллилитрах: '))
#     milk = int(input('Введите кол-во молока в миллилитрах: '))
#     coffee_machine = CoffeeMachine(coffee_beans, water, milk)

#     menu = Menu()
#     menu.options = CoffeeTypesList.coffee_types_list
#     menu.options.append('Выход')

#     while not menu.exit:
#         menu.print_menu()
#         if menu.handle_key() == "enter" and menu.exit is False:
#             menu_selected_index = menu.options[menu.selected_index]
#             if menu_selected_index != 'Выход':
#                 if menu_selected_index == 'craft':
#                     os.system("cls")
#                     craft_simple_coffee_count = int(input('Введите кол-во порций кофе: '))
#                     craft_water_count = int(input('Введите кол-во порций воды: '))
#                     craft_milk_count = int(input('Введите кол-во порций молока: '))
#                     coffee_machine.craft_params = (
#                         craft_simple_coffee_count,
#                         craft_water_count,
#                         craft_milk_count
#                     )
#                 print(coffee_machine.make_coffee(menu_selected_index))
#                 print(coffee_machine.get_left_count_of_coffee())
#                 print(coffee_machine.get_left_ingredients())
#                 sleep(5)
#             else:
#                 menu.exit_menu()


# if __name__ == '__main__':
#     main()

from fastapi import FastAPI
from src.api.routes import coffee_routes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Coffee Machine API")

app.include_router(coffee_routes.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
