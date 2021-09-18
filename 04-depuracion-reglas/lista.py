import pdb
pdb.set_trace()

def maximos(lista):
    '''
    Ejercicio leccion 4
    Haciendo uso de comprensión de listas realice un programa que,
    dado una lista de listas de números enteros, devuelva el máximo de cada lista.

    Metodo que devuelte los maximos de las sublistas recibidas.

    Inputs:
    --------
    lista --- Lista de multiples elementos.

    Output:
    --------
    Devuelve una lista con los elementos maximos de cada una de las sublistas.

    Ejemplo de uso:
    ---------------
    >>> lista = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    >>> print(maximos(lista))

    '''
    maximos = [max(i) for i in lista]
    return maximos


if __name__ == '__main__':
    lista = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    print(maximos(lista))
