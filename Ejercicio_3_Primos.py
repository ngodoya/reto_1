'''Escribir una función que reciba una lista de números y
devuelva solo aquellos que son primos.
La función debe recibir una lista de enteros y
retornar solo aquellos que sean primos.
'''



def solo_primos(lista: list) -> list:
    final_list = []

    for num in lista:
        
        if type(num) != int:
            raise ValueError("La lista solo debe tener enteros")
        prime = True
        for k in range(2, num):
            if num % k == 0:
                prime = False
                break
        if prime and num > 1:
            final_list.append(num)
      
    return final_list
print(solo_primos([7, 163, 1604, 1, 5, 2, 10]))