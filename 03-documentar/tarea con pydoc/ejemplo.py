def sumar(a, b):
    """Resuelve una suma de dos numeros.

    Devuelve el respultado de la suma:

        a+b


    Parametros:
    a -- primer numero a sumar
    b -- segundo numero a sumar

    Excepciones:
    ValueError -- Si (a == 0)

    """
    if a == 0:
        raise ValueError(
            'Coeficiente cuadrático no debe ser 0.')
    resultado = a+b

    return (resultado)

if __name__ == '__main__':
    print(sumar(5,4))