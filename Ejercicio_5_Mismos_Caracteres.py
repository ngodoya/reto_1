"""

Escribir una función que reciba una lista de string y 
retorne unicamente aquellos elementos que tengan los mismos 
caracteres. e.g. entrada: ["amor", "roma", "perro"], 
salida ["amor", "roma"]
"""

def mismos_caracteres(lista):
    dic = {}
    for word in lista:
        clave = ''.join(sorted(word))
        if clave in dic:
            dic[clave].append(word)
        else:
            dic[clave] = [word]
    result = []
    for group in dic.values():
        if len(group) > 1:
            result.extend(group)
    return result