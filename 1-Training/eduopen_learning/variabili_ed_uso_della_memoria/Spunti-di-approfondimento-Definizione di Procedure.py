"""
Santiago de Cali, Maggio 30 di 2020
Studente: William Martín Chávez González
A) Scrivere una procedura per disegnare un cerchio dato il centro e il raggio
con turtle.circle.
B) Scrivere una procedura per disegnare un quadrato, dato il centro, il lato
e l´orientazione.
C) Cambiare le procedure per disegnare cerchi inscritti nei quadrati.
"""
from turtle import *
import math

# A) Scrivere una procedura per disegnare un cerchio dato il centro e il raggio
# con turtle.circle.
home()
def cerchio(x_centro, y_centro, raggio):
    penup()
    goto(x_centro,y_centro)
    right(90)
    forward(raggio)
    left(90)
    pendown()
    circle(raggio)

cerchio(100,100,100)

# B) Scrivere una procedura per disegnare un quadrato, dato il centro, il lato
# e l´orientazione.
penup()
home()
def quadrato_orientato(x_centro, y_centro, lato, orientazione):
    penup()
    goto(x_centro, y_centro)
    right(orientazione)
    pendown()
    forward(lato)
    right(90)
    forward(lato)
    right(90)
    forward(lato)
    right(90)
    forward(lato)

quadrato_orientato(100,100,50,0)

# C) Cambiare le procedure per disegnare cerchi inscritti nei quadrati.
penup()
home()
def quadrato_inscritto_nel_cerchio(x_centro, y_centro, orientazione,raggio):
    goto(x_centro, y_centro)
    right(90)
    forward(raggio)
    left(90)
    pendown()
    circle(raggio)
    penup()
    goto(x_centro, y_centro)
    left(45)
    # ipotenusa = math.sqrt(math.pow(math.sin(45),2) + math.pow(math.cos(45),2))
    forward(raggio)
    right(135)
    lato = math.sin(math.pi/4)*2*raggio
    #pendown()
    #forward(lato)
    right(orientazione)
    pendown()
    forward(lato)
    right(90)
    forward(lato)
    right(90)
    forward(lato)
    right(90)
    forward(lato)

quadrato_inscritto_nel_cerchio(50,50,0,50)

done()