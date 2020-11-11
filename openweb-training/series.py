"""
Series:
- Strings
-
"""

# Strings:
catena = "Catena in Italiano"
for char in catena:
    print("Char - ", char)

# Operators:
print("b" in catena)
print("in" in catena)
print("Italiano" not in catena)

# Slice:
print(catena[2:5])
print(catena[2:7:2]) # From 2 to 6, every 2 characters
print(catena[:5])
catena[::-1] # Catena invertida

# Cast String:
num = str(6.5)
print(num)

"""
 Mutability properties:
"""

# - No mutability applies to strings:
oggetto_catena = "Ingegneria Informatica"
oggetto_catena.upper() #Metodo upper dell'oggetto catena
oggetto_catena[3] = "I" # ERROR - not support item assigment
oggetto_catena = oggetto_catena.upper() # Modifica l'oggetto catena
oggetto_catena = oggetto_catena.lower()
# Metodi per gli strings:
oggetto_catena.capitalize() # Première lettre capitale
oggetto_catena.upper() # Tutte la lettere
oggetto_catena.lower()
oggetto_catena.title() # Premiêre lettere de chaque mot
oggetto_catena.count("i")
oggetto_catena.count("e", 5)
oggetto_catena.count("e", 5, 8)
oggetto_catena.find("gn") # -1 if it is not there
oggetto_catena.startswith("In")
oggetto_catena.startswith("gn", 5)
oggetto_catena