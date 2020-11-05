"""
Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales y nos devuelva una lista sin las vocales, sin modificar la original.
"""

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vocals = ["a", "e", "i", "o", "u"]
new_abc = abc.copy()

for i in abc:
    for n in vocals:
        if i == n:
            new_abc.remove(i)

print(new_abc)