from pydantic import BaseModel, Field

class CoffeeMachineInit(BaseModel):
    coffee_beans: float = Field(..., gt=0, description="Количество кофейных зерен в граммах")
    water: float = Field(..., gt=0, description="Количество воды в миллилитрах")
    milk: float = Field(..., gt=0, description="Количество молока в миллилитрах")

class CraftCoffee(BaseModel):
    coffee_portions: int = Field(..., ge=0, description="Количество порций кофе")
    water_portions: int = Field(..., ge=0, description="Количество порций воды")
    milk_portions: int = Field(..., ge=0, description="Количество порций молока")

class CoffeeMachineStatus(BaseModel):
    coffee_beans: float
    water: float
    milk: float
    brewed_coffee_count: int
    remaining_brews: int

class CleaningResponse(BaseModel):
    message: str
    status: str