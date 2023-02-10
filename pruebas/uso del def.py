#USO DEL DEF (FUNCIONES)
number1 = int(input("Ingresar el valor numero 1:")) #primer numero
number2 = int(input("Ingresar el valor numero 2:")) #segundo numero
print(10 * "-")#ALGO DE USO ESTETICO 
def multiplicador(number1, number2): #CREAR UNA FUNCION Y LLAMAR A LAS VARIABLES
    if number2 < 0:
        return multiplicador(number1, number2)#RETURN se encargar de regresar los datos
    elif number2 == 0: #SI EL SEGUNDO NUMERO ES IGUAL A 0 ENTONCES EL RESULTADO OBVIO ES 0
        return 0 #LE DIGO QUE REGRESE UN 0 SI SE CUMPLE LA CONDICION
    elif number2 == 1: #SI EL SEGUNDO NUMERO ES IGUAL A 1 ENTONCES EL RESULTADO OBVIO ES EL MISMO NUMBER1
        return number1
    else:
        return number1 + multiplicador(number1, number2 - 1) #SI LO DEMAS NO SE CUMPLE LE DIGO QUE REGRESE EL NUMBER1 + LA FUNCION Y QUE LE RESTE 1 AL NUMERO2
print(multiplicador(number1,number2)) #LE DIGO QUE IMPRIMA LOS VALORES 