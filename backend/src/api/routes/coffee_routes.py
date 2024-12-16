from fastapi import APIRouter, HTTPException
from src.api.schemas.coffee_schemas import CleaningResponse, CoffeeMachineInit, CraftCoffee, CoffeeMachineStatus
from src.services.coffee_service import CoffeeMachineService

router = APIRouter(prefix="/coffee-machine", tags=["coffee-machine"])
coffee_service = None

@router.post("/initialize")
async def initialize_machine(params: CoffeeMachineInit):
    global coffee_service
    coffee_service = CoffeeMachineService(
        params.coffee_beans,
        params.water,
        params.milk
    )
    return {"message": "Кофе-машина инициализирована успешно"}

@router.post("/make/{coffee_type}")
async def make_coffee(coffee_type: str):
    if not coffee_service:
        raise HTTPException(status_code=400, detail="Кофе-машина не инициализирована")
    try:
        result = coffee_service.make_coffee(coffee_type)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/craft")
async def craft_coffee(params: CraftCoffee):
    if not coffee_service:
        raise HTTPException(status_code=400, detail="Кофе-машина не инициализирована")
    try:
        coffee_service.set_craft_params(
            params.coffee_portions,
            params.water_portions,
            params.milk_portions
        )
        result = coffee_service.make_coffee("craft")
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/status")
async def get_status():
    if not coffee_service:
        raise HTTPException(status_code=400, detail="Кофе-машина не инициализирована")
    return CoffeeMachineStatus(
        coffee_beans=coffee_service.get_coffee_beans(),
        water=coffee_service.get_water(),
        milk=coffee_service.get_milk(),
        brewed_coffee_count=coffee_service.get_brewed_count(),
        remaining_brews=coffee_service.get_remaining_brews()
    )


@router.post("/clean", response_model=CleaningResponse)
async def clean_machine():
    """
    Очистка кофе-машины и сброс счетчика приготовленных напитков
    """
    if not coffee_service:
        raise HTTPException(
            status_code=400, 
            detail="Кофе-машина не инициализирована"
        )
    try:
        result = coffee_service.clean_machine()
        return CleaningResponse(
            message=result,
            status="success"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при очистке кофе-машины: {str(e)}"
        )
