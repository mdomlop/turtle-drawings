#!/usr/bin/python
from turtle import *

posicion = pos()
angulo = 90
longitud = 100
separacion = 30
ramas = 8

nodo = [(posicion, angulo, longitud, separacion)]


def ramificar(n):
	p = n[0]
	h = n[1] + separacion
	l = n[2] * 0.71
	pu()
	goto(p)
	setheading(h)
	pd()
	fd(l)

	nuevopunto = (pos(), heading(), l)
	nodo.append(nuevopunto)
	

	h = h - separacion * 2
	pu()
	goto(p)
	setheading(h)
	pd()
	fd(l)

	nuevopunto = (pos(), heading(), l)
	nodo.append(nuevopunto)


speed(0)

sety(-100)

for i in range(2 ** ramas - 1):
	ramificar(nodo[i])

input(">")
