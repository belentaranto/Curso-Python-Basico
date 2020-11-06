"""
Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.
"""

print("Por favor ingrese sus datos personales")
name = input("Nombre: ")
age = input("Edad: ")
adress = input("Dirección: ")
phone = input("Teléfono: ")

info = {}

info.__setitem__("Name", name)
info.__setitem__("Age", age)
info.__setitem__("Adress", adress)
info.__setitem__("Phone", phone)

print(info)