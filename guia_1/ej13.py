"""
Ejercicio 13: Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

moneda = {
    'Euro':'€', 
    'Dolar':'$',
    'Yen':'¥'
}

msg = input("El símbolo de qué divisa querés saber?\n")
msg = msg.capitalize()

if msg in moneda:
    print(f"{msg} -> {moneda[msg]}")
else:
    print("No se ha encontrado la divisa solicitada")