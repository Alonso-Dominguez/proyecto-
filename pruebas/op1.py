def contar_productos(productos):
    total = 0  # valor inicial de la cuenta
    for cantidad in productos:
        total += cantidad  # agregar cada cantidad al total
    return total

# ejemplo de uso
productos = [10, 5, 2, 8, 3]  # lista de productos con sus cantidades
total = contar_productos(productos)
print("El total de productos es:", total)

#recibo
# Definir variables
nombre_cliente = input("Ingrese el nombre del cliente: ")
numero_cliente = int(input("Ingrese el número de cliente: "))
direccion_cliente = input("Ingrese la dirección del cliente: ")
lectura_anterior = int(input("Ingrese el número de lectura anterior: "))
lectura_actual = int(input("Ingrese el número de lectura actual: "))
tarifa_kilovatio = float(input("Ingrese la tarifa por kilovatio hora: "))

# Calcular kilovatios consumidos
kilovatios_consumidos = lectura_actual - lectura_anterior

# Calcular monto a pagar
monto_pagar = kilovatios_consumidos * tarifa_kilovatio

# Imprimir factura
print("Factura de luz\n")
print("Nombre del cliente:", nombre_cliente)
print("Número de cliente:", numero_cliente)
print("Dirección del cliente:", direccion_cliente)
print("Lectura anterior:", lectura_anterior)
print("Lectura actual:", lectura_actual)
print("Kilovatios consumidos:", kilovatios_consumidos)
print("Tarifa por kilovatio hora:", tarifa_kilovatio, "\n")
print("Monto a pagar: $", monto_pagar)
