def calculate() -> float:
    operation = input("Ingrese una operacion matematica: ")
    operation = operation.split()
    if (operation[1] == '+'):
        return (operation[0]+operation[2])