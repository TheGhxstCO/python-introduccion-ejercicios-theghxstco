"""
Título: Precio con IVA

Descripción:
Calcula el precio final de un producto con IVA del 19%.
"""

precio = float(input("Ingrese el precio del producto: "))
iva = precio * 0.19
total = precio + iva

print(f"El precio final con IVA es: {total}")