def convert_units(value, from_unit, to_unit):
    length_factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    
    weight_factors = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592
    }
    
    if from_unit in length_factors and to_unit in length_factors:
        factors = length_factors
    elif from_unit in weight_factors and to_unit in weight_factors:
        factors = weight_factors
    else:
        raise ValueError("Invalid or incompatible units.")
    
    base_value = value * factors[from_unit]
    result = base_value / factors[to_unit]
    
    return result
try:
    value = float(input("Enter the value: "))
    from_unit = input("Enter the unit to convert from: ").lower()
    to_unit = input("Enter the unit to convert to: ").lower()
    result = convert_units(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
except ValueError as e:
    print("Error:", str(e))
except Exception as e:
    print("An unexpected error occurred:", str(e))
