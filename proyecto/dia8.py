"""
Fecha:14/02/23
Nombre: José Alonso Domínguez Castillo 
Descripción: Cuantos años tienes
"""
print("Ingresar año actual: ")
año=int(input())
print("Ingresar año de nacimiento: ")
cumple=int(input())
edad= año - cumple
if año < 2023:
    print("Ingresar el año actual")
elif cumple < 1930:
    print("Ingresar un año superior a 1950")
elif año == 0:
    print(0)
elif cumple == 0:
    print(0)
else:
    print(("Tu edad es de"),edad,("años"))
