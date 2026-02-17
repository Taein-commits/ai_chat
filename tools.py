# tools.py

import math, io, contextlib

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

def python_executor(code: str):
    try:
        # Restrict builtins
        safe_globals = {
            "__builtins__": {
                "print": print,
                "range": range,
                "len": len,
                "int": int,
                "float": float,
                "str": str,
                "abs": abs,
                "min": min,
                "max": max,
                "sum": sum
            }
        }

        output_buffer = io.StringIO()

        with contextlib.redirect_stdout(output_buffer):
            exec(code, safe_globals)

        output = output_buffer.getvalue()

        return {"output": output if output else "Code executed successfully."}

    except Exception as e:
        return {"error": str(e)}
