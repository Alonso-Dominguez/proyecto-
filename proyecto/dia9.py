import random #importamos random
"""
Fecha: 15/02/23
Nombre: Jose Alonso Dominguez Castillo
"""
opciones = ["piedra","papel","tijeras",] #creamos una lista con nuestras opciones
fin = "fin"
while True:
    usuario = input("Elige piedra, papel o tijeras: ") #el usuario escoge una opcion escribiendola
    
    pc = random.choice(opciones) #pc tomar un valor aleatorio de la lista
    print(f"\nPC escoge  {pc}") #Imprimimos la opcion escogida por la PC

    if usuario == pc:
       print("Empate, ambos escogieron:", usuario)
    elif usuario == "piedra" and pc == "tijeras":
       print("Gana el usuario")
    elif usuario == "tijeras" and pc =="papel":
       print("Gana el usuario")
    elif usuario == "papel" and pc == "piedra":
       print("Gana el usuario")   
    elif usuario == "tijeras" and pc == "piedra":
       print("Gana PC") 
    elif usuario == "papel" and pc == "tijeras":
       print("Gana PC") 
    elif usuario == "piedra" and pc == "papel":
       print("Gana PC")    
    else:
        usuario == "fin"
        print("Fin del juego")
        break