"""
Título: Datos del usuario

Descripción:
Solicita nombre, edad y estatura y muestra los datos ingresados.
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))

print(f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura} m")