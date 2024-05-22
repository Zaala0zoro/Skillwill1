def convert_variable(var):
    if isinstance(var, str):
        try:
            converted_var = int(var)
            return converted_
        except ValueError:
            return f"Error: Cannot convert '{var}' to an integer."
    elif isinstance(var, int):
        return str(var)
    else:
        return "Error: Unsupported type."

