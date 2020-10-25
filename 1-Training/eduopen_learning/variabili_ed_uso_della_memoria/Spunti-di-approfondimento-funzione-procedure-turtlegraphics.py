"""
Santiago de Cali, Maggio 3, 2020
Studente: William Martín Chávez González
A) Dato il valore di tre segmenti, contenuto in altrettante variabili
a,b, e c, scrivere un comando per traccionare il segmento più lungo
usando turtle
B) Traccione una serie di cerchi, il 1ro con raggio r=2, il secondo con
raggio = 4, il terzo con raggio r=8, etc. Utilizzare la funzione pow e
la procedura turtle.circle(raggio)
"""

# A) Risultato:
from turtle import *
segmento_a = 34
segmento_b = 24
segmento_c = 10
penup()
left(90)
forward(100)
right(45)
pendown()
forward(max(segmento_a, segmento_b, segmento_c))

# B) Risultato
raggio = 2
penup()
home()
pendown()
circle(raggio)
raggio_2 = pow(raggio, 2)
circle(raggio_2)
raggio_3 = pow(raggio, 3)
circle(raggio_3)