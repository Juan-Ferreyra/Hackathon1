def calculate(expression: str) -> float:
    expression = expression.strip()

    if not expression:
        raise ValueError("La expresión está vacía.")

    try:
        if "/" in expression:
            partes = expression.split("/")
            if len(partes) != 2:
                raise SyntaxError("Expresión de división no válida.")

            izquierda = float(partes[0].strip())
            derecha = float(partes[1].strip())

            if derecha == 0:
                raise ZeroDivisionError("División por cero.")

            return izquierda / derecha
        else:
            raise NotImplementedError("Solo se admite división por ahora.")

    except ValueError:
        raise ValueError("Carácter inválido en la expresión.")
