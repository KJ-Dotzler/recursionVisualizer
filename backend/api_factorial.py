from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Dict

router = APIRouter()

class FactorialInput(BaseModel):
    n : int = Field(gt=0)

class execStep(BaseModel):
    line: int
    event: str
    description: str
    n: int
    returnVal: int | None = None

class FactorialOutput(BaseModel):
    steps : List[execStep]

def factorialSteps(n : int, steps : List[execStep]) -> int:
    steps.append(
        execStep(
            line=1, 
            event='call', 
            description=f'Entering factorial({n})',
            n=n,
            )
        )
    steps.append(
        execStep(
            line=2, 
            event='check_base', 
            description=f'Checking if n <= 1',
            n=n,
            )
        )
    
    if n <= 1:
        steps.append(
            execStep(
                line=3,
                event='return', 
                description='Base case reached, returning 1',
                n=n,
                returnVal=1
                )
            )
        return 1
    steps.append(
        execStep(
            line=4, 
            event='evaluate_recursive', 
            description=f'Evaluating factorial({n-1})',
            n=n,
            )
        )
    
    childVal = factorialSteps(n-1, steps)
    result = n * childVal
    steps.append(
        execStep(
            line=4,
            event='substitute', 
            description=f'Substituting returned value {childVal} into {n} * {childVal}',
            n=n,
            returnVal=result))
    
    steps.append(
        execStep(
            line=4, 
            event='return', 
            description=f'Returning {result}',
            n=n,
            returnVal=result
            )
        )
    return result

@router.post('/factorial', response_model=FactorialOutput)
def factorial_endpoint(data:FactorialInput):
    steps: List[execStep] = []
    factorialSteps(data.n, steps)
    return FactorialOutput(steps=steps)
