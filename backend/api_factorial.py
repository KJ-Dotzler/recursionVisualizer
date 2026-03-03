from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Dict

router = APIRouter()

class FactorialInput(BaseModel):
    n : int = Field(gt=0)

class Step(BaseModel):
    action: str
    value: str
    depth: int
    n: int
    returnVal: int | None = None

class FactorialOutput(BaseModel):
    steps : List[Step]

def factorialSteps(n : int, steps : List[Step], depth: int = 0) -> int:
    steps.append(
        Step(
            action='call', 
            value=f'Factorial({n})', 
            depth=depth,
            n=n,
            returnVal=None
            )
        )
    if n <= 1:
        steps.append(
            Step(
                action='return',
                value=f'1', 
                depth=depth,
                n=n,
                returnVal=1
                )
            )
        return 1
    else:
        result = n * factorialSteps(n-1, steps, depth + 1)
        steps.append(
            Step(
                action='return',
                value=f'{result}', 
                depth=depth,
                n=n,
                returnVal=result))
        return result

@router.post('/factorial', response_model=FactorialOutput)
def factorial_endpoint(data:FactorialInput):
    steps: List[Step] = []
    factorialSteps(data.n, steps)
    return FactorialOutput(steps=steps)
