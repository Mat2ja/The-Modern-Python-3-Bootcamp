def calculate(make_float, operation, first=0, second=0, message="The result is"):
    operations = {
        'add': first + second,
        'subtract': first - second,
        'divide': first / second,
        'multiply': first * second,
    }
    
    result = operations[operation]
    
    if make_float:
        result = float(result)
    else:
        result = int(result)
        
    return message + " " + str(result)



print(calculate(make_float=False, operation='add',
                message='You just added', first=2, second=4))  # "You just added 6"
print(calculate(make_float=True, operation='divide',
                first=3.5, second=5))  # "The result is 0.7"
