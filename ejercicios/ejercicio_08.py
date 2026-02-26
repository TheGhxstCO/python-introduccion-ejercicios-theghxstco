"""
Ejercicio 08 - Iteración de colecciones
Recorrer una lista y un diccionario.
"""

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"Número: {numero}")

persona = {"nombre": "Ana", "edad": 22}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")