#!/usr/bin/python3
# Dibuja un cuadrado

import turtle

llado = 100
lados = 1

def dibujar():
	print("¿Cuántos lados?")
	lados = input("> ")
	lados = int(lados)

	angulo = (lados - 2) * 180 / lados
	angulo = 180 - angulo

	turtle.reset()
	while lados > 0:
		turtle.fd(llado)
		turtle.lt(angulo)
		lados = lados - 1

while lados != 0:
	dibujar()
