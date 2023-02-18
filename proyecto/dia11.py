"""
Fecha: 17/02/23
Nombre: José Alonso Domínguez Castillo
"""
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
