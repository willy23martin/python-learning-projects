# Placeholders: replace the string segment value using variables

name = "Willy23"
sentence = "%s is 15"
sentence%name
sentence%("Pepito")

#Second example:
sentence = "%s %s is the president of U.S"
sentence%("Pepito", "Perez")

#Third example using %d for decimals:
sentence = "%s is %d years old"
sentence%("Pepito", 50)
sentence2 = sentence%("Pepita", 29)