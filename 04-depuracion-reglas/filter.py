'''
    Ejercicio b leccion 4
    Haga uso de la función filter para construir un programa que,
    dado una lista de n números devuelva aquellos que son primos
'''
import pdb
pdb.set_trace()


def es_primo(n):
    '''
    Metodo que devuelte true si es primo.

    Inputs:
    --------
    n --- numero sobre el que verificamos si es primo.

    Output:
    --------
    Devuelve True o False.

    Ejemplo de uso:
    ---------------
    >>> print(es_primo(5))

    '''
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


lista = [3, 4, 8, 5, 5, 22, 13]
# Usamo filter y list para obtener la lista de primos llamando a la funcion es_primo
print(list(filter(es_primo, lista)))
