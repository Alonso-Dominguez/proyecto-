"""
Fecha: 27/02/23
Nombre: José Alonso Domínguez Castillo
"""
usuario=input()
while usuario == "Hola":
  print("Hola, mi nombre es Mary")
  break
usuario=input()
while usuario== "¿Como estas?":
  print("Yo muy bien, espero tu tambien lo estes")
  break
while usuario== "Necesito que me hagas una operación":
  print("Claro, ¿que clase de opreración?")
  break
while usuario== "Suma":
  print("Claro!, dime tus numeros")
  break
numero1=input()
numero2=input()
suma= numero1 + numero2
print("El resultado es ",suma)