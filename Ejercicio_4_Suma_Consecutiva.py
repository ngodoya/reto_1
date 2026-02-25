"""
Escribir una función que reciba una lista de números enteros 
y retorne la mayor suma entre dos elementos consecutivos.
"""

def suma_consecutiva(lista: list) -> int | str:
    if len(lista) < 2:
        return 'La lista debe tener 2 elementos al menos'
    
    maxim = lista[0] + lista[1]
    for elemento in lista:
        if type(elemento) != int:
            return 'la lista solo debe tener Enteros'
    for i in range(len(lista)-1):
        sum_current = lista[i+1] + lista[i]
        
        if sum_current > maxim:
            maxim= sum_current

    return maxim

print(suma_consecutiva([7,163,1604,1,5,2,10]))