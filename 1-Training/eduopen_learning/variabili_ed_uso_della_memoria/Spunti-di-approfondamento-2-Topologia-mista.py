# Il valore usato per la definizione della varibile determina suo tipo
# Preparare a definire variabili utilizzando numeri <<interi>> e <<reali>>
# A) Che cosa succede calcilando espressioni con variabili dello stesso tipo?
# B) E di tipo misto?

# A) Con i numeri interi:
aliquota = 0.22 # 22%
prezzo_compresivo = 100
prezzo_netto = prezzo_compresivo / (1 + 1*aliquota) # fratto 1.22
print(prezzo_netto)

# B) Con i numeri reali:
aliquota = 0.22 # 22%
prezzo_compresivo = 100.00
prezzo_netto = prezzo_compresivo / (1 + 1*aliquota) # fratto 1.22
print(prezzo_netto)

# Il valore usato per la definizione della varibile determina suo tipo
# Preparare a definire variabili utilizzando numeri <<interi>> e <<reali>>
# A) Che cosa succede calcilando espressioni con variabili dello stesso tipo?
# B) E di tipo misto?

# A) Con numeri interi:
altezza = 5
base = 10
area_triangolo = base * altezza / 2 # Base per altezza fratto due
print(area_triangolo)

# A) Con numeri reali:
altezza = 5.0
base = 10.0
area_triangolo = base * altezza / 2.0 # Base per altezza fratto due
print(area_triangolo)