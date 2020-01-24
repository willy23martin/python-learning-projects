# Arithmetic operators

age1, age2 = 12, 18
print("The sum is: ", age1 + age2)
print("The substraction is: ", age1 - age2)
print("The product is: ", age1 * age2)
print("The division is: ", age1 / age2)
print("The modulus is: ", age1 % age2)

#String operators

firstName, lastName = "Albin", "Ardillas"
print("Complete name: ", firstName + " " + lastName)
print("Repeat string patterns: ", "PatternX" * 5) #Multiply string pattern
# Every string character in a string has an index, started by 0, so:
sentence2 = "Albin y las ardillas son excelentes"
print("First sentence character: ", sentence2[0])
print("First sentence segment: ", sentence2[0:7]) #"Albin y" - character 0 to character (n-1)
print("First three characters: ", sentence2[:3]) #Alb
print("All the sentence but until the last five characters: ", sentence2[:-5]) #"Albin y las ardillas son excel"