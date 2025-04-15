def calculate(operation) -> float:
    
    operation = operation.split()

    if (operation[1] == "-"):
        return int(operation[0]) - int(operation[2])
