"""""
Fecha:08/02/23
Nombre: Jose Alonso Dominguez Castillo
"""
#aplicacion que pueda sumar, multiplicar, dividir y restar
print("Insertar numeros")#texto que indique que poner en la aplicacion
n1=int(input("Numero 1: "))#valor que el usuario ingresa 
n2=int(input("Numero 2: "))#valor que el usuario ingresa
suma= n1 + n2#operacion que se realizara
resta= n1 - n2#operacion que se realizara
multi= n1 * n2#operacion que se realizara
division= n1 / n2#operacion que se realizara
print("Suma: ",suma, "Resta: ",resta, "Multiplicacion: ",multi, "Division: ",division)#resultados que mostrara al usuario

print("{} + {} =".format(n1,n2),(n1 + n2))
print("{} - {} =".format(n1,n2),(n1 - n2))
print("{} * {} =".format(n1,n2),(n1 * n2))
print("{} / {} =".format(n1,n2),(n1 / n2))