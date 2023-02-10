"""
Fecha: 09/02/23
Nombre: Jose Alonso Dominguez Castillo
"""
def mayor(numero1, numero2 , numero3):
    result=None
    if numero1 < numero2 < numero3:
        result=numero3
    if numero1 < numero2 > numero3:
        result=numero2
    if numero1 > numero2 > numero3:
        result=numero1
    return result
print(1,2,3)
print(3,2,1)
print(2,1,3)
print(3,1,2)
print(1,3,2)
print(1,1,1)
print(2,2,2)
print(3,3,3)