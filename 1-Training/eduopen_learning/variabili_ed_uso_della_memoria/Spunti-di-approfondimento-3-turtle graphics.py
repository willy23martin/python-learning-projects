"""
Santiago de Cali, Maggio 3 di 2020
Studente: William Martín Chávez González
Spunti di approfondimento:
A) Scrivere programmi per tracciare figure geometriche. Utilizzare variabili ed espressioni come
argomento dei comandi per la tartaruga.
"""
# Piazza:
from turtle import *
import math
lato = 100
angolo = 90
penup()
right(angolo)
forward(lato)
left(angolo)
forward(lato)
left(angolo)
pendown()
forward(lato)
left(angolo)
forward(lato)
left(angolo)
forward(lato)
left(angolo)
forward(lato)

# Triangolo:
gamba_opposta = 100
gamba_adiacente = 50
ipotenusa = math.sqrt(gamba_opposta**2 + gamba_adiacente**2)
penup()
left(135)
forward(400)
pendown()
left(135)
forward(gamba_opposta)
left(90)
forward(gamba_adiacente)
left(117)
forward(ipotenusa)

# Cerchio:
radio = 14
diametro = radio * 2
penup()
left(180-(117-90))
forward(300)
pendown()
circle(diametro)
done()


