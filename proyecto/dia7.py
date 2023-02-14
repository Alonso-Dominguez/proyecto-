"""
Fecha:13/02/23
Nombre:Jose Alonso Dominguez Castillo
"""
print("Cuenta a pagar")#texto que informa los datos que saldran
Hamburguesa= 40#valor del producto
Hotdog= 25#valor del producto
Tacos= 15#valor del producto
Tortas= 20#valor del producto
Alitas= 80#valor del producto
productos=["Hamburguesa= 40","Hotdog= 25","Tacos= 15","Tortas= 20","Alitas= 80",]#lista de productos junto con sus precios 
precios=[Hamburguesa,Hotdog,Tacos,Tortas,Alitas]#precios o valores de los productos
total = Hamburguesa+Hotdog+Tacos+Tortas+Alitas#operacion que se realizara para el total a pagar
print("Alimentos consumidos:")#texto que informa los datos que saldran
for producto in productos:#condicion que se realizara
    print(producto)#valor que se imprimira
print(25 * "_")#decoracion
print("El total a pagar es: ",total)#texto que se imprimira junto al valor total de los precios