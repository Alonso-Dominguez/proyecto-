def contar_productos(productos):
    total = 0  # valor inicial de la cuenta
    for cantidad in productos:
        total += cantidad  # agregar cada cantidad al total
    return total

# ejemplo de uso
productos = [10, 5, 2, 8, 3]  # lista de productos con sus cantidades
total = contar_productos(productos)
print("El total de productos es:", total)
