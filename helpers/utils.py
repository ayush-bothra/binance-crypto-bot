from typing import List

def get_valid_input(
        request: str, 
        valid_options: List[str]=None
    ) -> str:
    while True:
        user_input = input(request).strip().upper()
        if not user_input:
            print("User input cannot be empty")
            continue
        
        if valid_options and user_input not in valid_options:
            print(f"Invalid!, choose from: {', '.join(valid_options)}")
            continue
        
        return user_input
    
def get_valid_float(request: float) -> float:
    while True:
        try:
            value = float(input(request))
            if value <= 0:
                print("Quantity must be positive")
                continue
            return value
        except ValueError:
            print("Invalid number. Enter a decimal")
            
def format_quantity(value, precision=3):
    """
     format_quantity(0.0019, 3) -> 0.001
    """
    factor = 10 ** precision
    floored_value = int(value * factor) / factor
    return "{:.{prec}f}".format(floored_value, prec=precision)