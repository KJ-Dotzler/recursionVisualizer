from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class FactorialInput(BaseModel):
    n : int
    pass

class Step(BaseModel):
    action : str
    value : str

class FactorialOutput(BaseModel):
    output = List[Step]

def factorialSteps(n : int, steps : List[Step]) -> int:
    steps.append(Step(action='call', value=f'Factorial{n}'))
    if n <= 1:
        steps.append(Step(action='return',value='1'))
        return 1
    else:
        result = n * factorialSteps(n-1, steps)
        steps.append(Step(action='return',value=str(result)))
        return result