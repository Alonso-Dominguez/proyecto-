"""
Fecha: 20/02/23
Nombre: Jose Alonso Dominguez Castillo
"""
print("Insertar partidos ganados")
ganados= int(input())
print("Insertar partidos empatados")
empate= int(input())
print("Insertar partidos perdidos")
perdidos= int(input())
puntos= ganados * 2 + empate - perdidos
print("Puntos totales del equipo: ",puntos)