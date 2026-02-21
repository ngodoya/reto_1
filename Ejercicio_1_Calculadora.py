"""
Ejercicio 1 - Calculadora básica

Crear una función que realice operaciones básicas
(suma, resta, multiplicación, división) entre dos números,
según la elección del usuario.
"""

valid_operators = ('+', '-', '*', '/')

def calculadora(num1: float, num2: float, operator: str) -> float | str:
    
    if type(operator) is str:
        
        if operator in valid_operators:
            
            if operator == '+':
                return num1 + num2
            
            elif operator == '-':
                return num1 - num2
            
            elif operator == '*':
                return num1 * num2
            
            elif operator == '/':
                if num2 == 0:
                    return 'No se puede dividir por 0'
                return num1 / num2
        
        else:
            return 'Ingrese una operacion permitida (+,-,*,/)'
    
    return 'Ingrese una operación valida'


if __name__ == "__main__":
    print(calculadora(1, 2, "+"))  