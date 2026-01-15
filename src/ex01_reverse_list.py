"""
EX01 (Listas)
Invertir una lista sin modificar la original.
"""

def reverse_list(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista con los elementos de `values` en orden inverso.
    - No modifica la lista original.
    """
    # Usamos slicing para crear una nueva lista invertida
    return values[::-1]