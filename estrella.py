#!/usr/bin/python3
# Dibuja un cuadrado

from turtle import *

llado = 100

print("¿Cuántas puntas?")
puntas = input("> ")
puntas = int(puntas)

angulo = (puntas - 2) * 180 / puntas
angulo = 180 - angulo
angulo = angulo * 2

while puntas > 0:
	fd(llado)
	lt(angulo)
	puntas = puntas - 1

