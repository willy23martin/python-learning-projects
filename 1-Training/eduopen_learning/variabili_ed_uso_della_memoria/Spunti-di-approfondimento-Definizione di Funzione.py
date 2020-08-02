"""
Santiago de Cali, Giugno 29 di 2020
Studente: William Martín Chávez González
A) Scrivere funzioni per calcolare perimetri e aree di figure geometriche.
B) Scrivere una funzione per calcolare il prezzo al netto dell`IVA, dato
il prezzo lordo e l`aliquota.
C) Scrivere una funzione che calcola la distanza della tartaruga dal centro del pannello.
"""

#A) Scrivere funzioni per calcolare perimetri e aree di figure geometriche.

#A1) Cerchio:
import math
def perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

def area_cerchio(raggio):
    return math.pi * (raggio ** 2)

#A2) Cuadrato:
def perimetro_cuadrato(lato):
    return lato*4

def area_cuadrato(lato):
    return lato**2

#A3) Triangolo:
def perimetro_triangolo(latoA, latoB, latoC):
    return latoA + latoB + latoC

def area_triangolo(base, altezza):
    return (base*altezza)/2

print(perimetro_cerchio(1))
print(area_cerchio(1))
print(perimetro_cuadrato(2))
print(area_cuadrato(3))
print(perimetro_triangolo(4,5,6))
print(area_triangolo(9,10))