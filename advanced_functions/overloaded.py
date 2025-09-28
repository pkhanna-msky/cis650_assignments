from math import pi
from typing import Optional, Union

def area(*args: Union[int, float, str]):
    """
    Simulate overloading by ARITY (number of args) and TYPE.
    - area(side)                  -> area of a square
    - area(length, width)         -> area of a rectangle
    - area(radius, "circle")      -> area of a circle
    """
    if len(args) == 1 and isinstance(args[0], (int, float)):
        side = float(args[0])
        return side * side
    
    if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
        length = float(args[0])
        width = float(args[1])
        return length * width

    if (
        len(args) == 2 
        and isinstance(args[0], (int, float)) 
        and isinstance(args[1], str) 
        and args[1].lower() == "circle"
    ):
        radius = float(args[0])
        return pi * (radius ** 2)
    
    raise TypeError("Usage: area(side) | area(length, width) | area(radius, 'circle')")
    
def greet(name: Optional[str] = None) -> str:
    """Simulate overloading by DEFAULT PARAMETER."""
    return f"Hello, {name}!" if name else "Hello!"

if __name__ == "__main__":
    print("Simulated overloading examples:\n")
    print("1) area(5) [square] =", area(5))
    print("2) area(5, 3) [rectangle] =", area(5, 3))
    print("3) area(2, 'circle') =", round(area(2, "circle"), 4))
    print("4) greet() =", greet())
    print('5) greet("Alex") =', greet("Alex"))
        
