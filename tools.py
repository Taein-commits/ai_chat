# tools.py

import math

def calculator(expression: str):
    try:
        # Safe evaluation
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round
        }
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

def bmi(height_cm: float, weight_kg: float):
    try:
        height_m = height_cm / 100
        bmi_value = weight_kg / (height_m ** 2)
        return {"bmi": round(bmi_value, 2)}
    except Exception as e:
        return {"error": str(e)}
