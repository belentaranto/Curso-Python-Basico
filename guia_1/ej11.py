"""
Ejercicio 11: Crear una lista con varios números, luego ordenarlos de manera creciente y devolver por pantalla la lista ordenada y cuál es el menor y cuál el mayor.
"""

nums = [3, 90, 13, 78, 23, 109, 4, 6]
ord_nums = sorted(nums)

print(ord_nums)
print(f"El menor es {ord_nums[0]}")
print(f"El mayor es {ord_nums[-1]}")