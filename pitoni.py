def convert_variable(var):
    if isinstance(var, str):
        try:
            converted_var = int(var)
        except ValueError:
            raise ValueError(f"Cannot convert string '{var}' to an integer.")
    elif isinstance(var, int):
        converted_var = str(var)
    else:
        raise TypeError(f"Unsupported variable type: {type(var)}")

    return converted_var


var1 = "1105"
var2 = 2004

converted_var1 = convert_variable(var1)
converted_var2 = convert_variable(var2)

print(converted_var1)
print(converted_var2)
