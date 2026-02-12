"""
Título: Saludo Personalizado

Descripción:
Solicita el nombre y la edad del usuario y muestra un saludo personalizado.

Requisitos:
1. Pedir el nombre.
2. Pedir la edad.
3. Mostrar un mensaje usando f-strings.
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Hola {nombre}, tienes {edad} años.")