"""
Ejercicio 16: Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

info = {}
rta = "si"

while rta.capitalize() == "Si":
    k = input("Qué dato desea ingresar? ")
    v = input(f"{k.capitalize()}: ")
    info.__setitem__(k,v)
    print(info)
    rta = input("Desea agregar algo más? ")
print("El ingreso de datos finalizó")