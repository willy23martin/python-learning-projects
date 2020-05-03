"""
Santiago de Cali, Giovedi, 30 di aprile, 2020
 Studente: William Martin Chávez González
 Spunti di Approfondimento
 Calcolatre un prezzo al netto dell`IVA a partire dal prezzo compresivo di IVA (supporre l´aliquota del 22%):
 Questo processo è chiamato lo scorporo:
 1) Prima, il prezzo compresivo si puoi separarlo:
 aliquota = 0.22 --> 22%
 prezzo_compresivo = prezzo_netto + prezzo_netto * aliquota
 prezzo_compresivo = prezzo_netto * (1 + 1*0.22)
 prezzo_compresivo = prezzo_netto * (1.22)
 prezzo_netto = prezzo_compresivo / 1.22
"""
aliquota = 22 / 100
prezzo_compresivo = 158.6
prezzo_netto = prezzo_compresivo / (1 + 1*aliquota)
print(prezzo_netto)

# Si può utilizzare una variable chiamata nel punto A: aliquota.

# Riferimenti bibliografici:
# 1) https://www.soldioggi.it/come-calcolare-iva-22-per-cento-8087.html