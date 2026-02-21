# Reto_1
Este repositorio contiene la solución a los 5 ejercicios propuestos en clase.
Cada ejercicio se encuentra en un archivo independiente.

---

## Ejercicio 1 - Calculadora
Para desarrollar este ejercicio se utilizaron estructuras condicionales (if y elif) para evaluar qué operación matemática debe ejecutarse según el operador ingresado por el usuario.

Primero se definieron las operaciones permitidas dentro de una tupla, ya que este tipo de colección es inmutable. Esto evita que las operaciones puedan modificarse accidentalmente durante la ejecución del programa.

Posteriormente se validó:
- Que el operador ingresado sea un str.
- Que el operador pertenezca a las operaciones permitidas (+, -, *, /).
- Que en caso de división, el segundo número no sea cero.
Si alguna validación falla, la función retorna un mensaje descriptivo indicando el error.