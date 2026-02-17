# tool_registry.py

from tools import calculator, bmi, python_executor

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression like 2+3*4"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bmi",
            "description": "Calculate BMI from height (cm) and weight (kg).",
            "parameters": {
                "type": "object",
                "properties": {
                    "height_cm": {"type": "number"},
                    "weight_kg": {"type": "number"}
                },
                "required": ["height_cm", "weight_kg"]
            }
        }
    },
    
    {
        "type": "function",
        "function": {
            "name": "python_executor",
            "description": "Execute safe Python code and return output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Python code to execute"
                    }
                },
                "required": ["code"]
            }
        }
    }
]

TOOL_FUNCTIONS = {
    "calculator": calculator,
    "bmi": bmi,
    "python_executor": python_executor
}
