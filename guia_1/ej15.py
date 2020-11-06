"""
Ejercicio 15: Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""

materias = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

for i,k in materias.items():
    print(f"{i} tiene {k} créditos")
print(f"El curso tiene en total {sum(materias.values())} créditos")