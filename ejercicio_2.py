from functools import reduce


def es_impar(numero):
    return True if numero % 2 != 0 else False

def sumar_impares(lista_numeros: list) -> int:
    numeros_impares = filter(es_impar, lista_numeros)
    suma_impares = reduce((lambda x,y: x + y), numeros_impares)
    
    return suma_impares

suma = sumar_impares([1,2,3,4,5,6,7,8,9])

print(suma)
