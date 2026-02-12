"""
Título: Promedio de tres notas

Descripción:
Calcula el promedio de tres notas ingresadas por el usuario.
"""

nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))

promedio = (nota_1 + nota_2 + nota_3) / 3

print(f"El promedio es: {promedio}")