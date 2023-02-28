"""
Fecha: 23/02/22
Nombre: José Alonso Domínguez Castillo
"""
x= ["O","R","S","J","O","Z","R"]
y= ["0","1","2","3","4","5","6"]
print(x)
print(y)
fin= "fin"
while True: 
    usuario= input("Forma una palabra usando los numeros:")
    if usuario== "0""3""4" or "4""3""0":
        print("OJO")
    elif usuario== "5""0""1""6""4" or "5""4""6""1""0":
        print("ZORRO")
    elif usuario== "6""0""3""4" or "6""4""3""0" or "1""0""3""4":
        print("ROJO")
    elif usuario== "0""1""4" or "4""1""0" or "0""6""4" or "4""6""0":
        print("ORO")
    else:
        usuario=="fin"
        break