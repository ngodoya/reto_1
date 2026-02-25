'''
Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra 
y verificar que sea igual a la original.
'''

def palindromo(word: str) -> bool:
    word = word.lower().replace(' ', '')
    begin = 0
    end = len(word) - 1

    while begin < end:
        if word[begin] != word[end]:
            return False
        begin += 1
        end -= 1
    return True
print(palindromo("Dabale arroz a la zorra el abad"))