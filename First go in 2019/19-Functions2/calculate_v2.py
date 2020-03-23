def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs['first'] + kwargs['second'],
        'subtract': kwargs['first'] - kwargs['second'],
        'divide': kwargs['first'] / kwargs['second'],
        'multiply': kwargs['first'] * kwargs['second'],
    }

    is_float = kwargs.get('make_float', False)
    result = operation_lookup[kwargs.get('operation', '')]

    if is_float:
        result = float(result)
    else:
        result = int(result)

    return f"{kwargs.get('message','The result is')} {result}"

