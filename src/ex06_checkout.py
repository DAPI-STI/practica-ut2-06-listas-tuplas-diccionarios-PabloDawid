"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

PRICES: dict[str, float] = {
    "Pan": 1.40,
    "Huevos": 2.30,
    "Cebolla": 0.85,
    "Aceite": 4.35,
}

PRICES: dict[str, float] = {
    "Pan": 1.40,
    "Huevos": 2.30,
    "Cebolla": 0.85,
    "Aceite": 4.35,
}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general
    """
    if not cart:
        return {}, 0.0

    totals: dict[str, float] = {}

    for product, units in cart:
        if units < 0:
            raise ValueError("Las unidades no pueden ser negativas.")
        if product not in PRICES:
            raise ValueError(f"Producto desconocido: {product}")

        totals[product] = totals.get(product, 0.0) + PRICES[product] * units

    # 🔧 Redondear cada subtotal y el total general
    for product in totals:
        totals[product] = round(totals[product], 2)

    total_general = round(sum(totals.values()), 2)
    return totals, total_general