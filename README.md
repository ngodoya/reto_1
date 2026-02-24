# Reto_1
Este repositorio contiene la solución a los 5 ejercicios propuestos en clase.
Cada ejercicio se encuentra en un archivo independiente.

---

## Ejercicio 1 - Calculadora
[Ver Código](./Ejercicio_1_Calculadora.py)

Para desarrollar este ejercicio se utilizaron estructuras condicionales (if y elif) para evaluar qué operación matemática debe ejecutarse según el operador ingresado por el usuario.

Primero se definieron las operaciones permitidas dentro de una tupla, ya que este tipo de colección es inmutable. Esto evita que las operaciones puedan modificarse accidentalmente durante la ejecución del programa.

Posteriormente se validó:
- Que el operador ingresado sea un str.
- Que el operador pertenezca a las operaciones permitidas (+, -, *, /).
- Que en caso de división, el segundo número no sea cero.
Si alguna validación falla, la función retorna un mensaje descriptivo indicando el error.

--- 

## Ejercicio 2 - Palindromos

[Ver Código](./Ejercicio_2_Palindromo.py)

La funcion debe de recibir la palabra y convertirla toda en minuscula para que no tengamos problema, en casos donde lleguemos a considerar A != a, esto pasa porque no tienen el mismo numero asignado por Unicode.

Se utiliza la función len() para determinar la longitud de la cadena y establecer los índices inicial y final. Es necesario restar 1 a la longitud porque en Python los índices comienzan en 0; de lo contrario, se produciría un error de índice fuera de rango (IndexError).

El ciclo while compara los caracteres desde los extremos hacia el centro. Si en algún momento los caracteres comparados son distintos, la función retorna False. Si todas las comparaciones coinciden, se retorna True.
(Remarcar que este algortimo tiene error cuando se trata de trabajar con palindromos que contengan tildes).

---

## Ejercicio 3 - Primos

[Ver Código](./Ejercicio_3_Primos.py)
Este ejercicio resultó más complejo debido a que fue necesario utilizar un ciclo for dentro de otro para evaluar cada número de la lista y verificar si es primo.

El punto clave fue el uso del operador módulo (%), el cual devuelve el residuo de una división. Si un número es divisible por otro, el resultado del módulo es 0. A partir de esta propiedad, se puede determinar si un número tiene divisores distintos de 1 y de sí mismo.

Recordando que un número primo se define como aquel que solo es divisible por 1 y por sí mismo, se evaluó cada número probando posibles divisores. Si en algún momento el residuo es 0, se descarta como primo.

Es importante considerar que el número 1 no es primo, ya que no cumple con la definición matemática de número primo. 