"""
Santiago de Cali, Giugno 29 di 2020
Studente: William Martín Chávez González
A) Scrivere funzioni per calcolare perimetri e aree di figure geometriche.
B) Scrivere una funzione per calcolare il prezzo al netto dell`IVA, dato
il prezzo lordo e l`aliquota.
C) Scrivere una funzione che calcolare la distanza della tartaruga dal centro del pannello.
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

print("Perimetro del cerchio di raggio 1 è: " , perimetro_cerchio(1))
print("L'area del cerchio con raggio `e: ", area_cerchio(1))
print("Il perimetro del cuadrato è:", perimetro_cuadrato(2))
print("L'area del cuadrato è:", area_cuadrato(3))
print("Il perimetro del triangolo è: ", perimetro_triangolo(4, 5, 6))
print("L'area del triangolo è:", area_triangolo(9, 10))

"""
B) Scrivere una funzione per calcolare il prezzo al netto dell`IVA, dato
il prezzo lordo e l`aliquota.
Riferimento: https://debitoor.it/blog/prezzo-lordo-e-netto-nel-modello-di-fattura#:~:text=Prezzo%20netto%20vs%20prezzo%20lordo,le%20imposte%20o%20eventuali%20ritenute.
"""
# Si definisce il prezzo lordo quello che ha l´IVA:
def calcolare_prezzo_al_neto(prezzo_lordo, aliquota):
    prezzo_neto = prezzo_lordo / (1 + (aliquota/100))
    return prezzo_neto

print("Il prezzo netto è:", calcolare_prezzo_al_neto(122, 22))

# C) Scrivere una funzione che calcolare la distanza della tartaruga dal centro del pannello:

def calcolare_distanza_tartaruga_centro_pannello(x, y):
    return math.sqrt((x**2) + (y**2))

print("La distanza della tartaruga dal centro del panello è: " , calcolare_distanza_tartaruga_centro_pannello(3,4))