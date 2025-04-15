def calculate(operation) -> float:
    operation = operation.split()
    if (operation[1] == '+'):
        return (operation[0]+operation[2])

    elif (operation[1] == "-"):
        return int(operation[0]) - int(operation[2])

