import datetime

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()

# Verificar si el mes es marzo o no
if fecha_actual.month == 3:
    print("La fecha actual es en marzo.")
else:
    print("La fecha actual no es en marzo.")
