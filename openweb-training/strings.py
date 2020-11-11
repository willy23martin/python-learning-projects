"""
Strings are not mutable
"""

simple = 'Simple string'
simpleII = "Simple string"
complex = '''
complex string
'''

concat = simple + simpleII
print(concat)
index = simple[3]
print(index)
repetition = concat*3
print(repetition)
print(len(index))

# UNICODE character comparison:
print("a" > "A")

print(complex.upper()) # Returns a new string but does not modify the string value
print(complex)

"""
Metodi:
"""
print("Metodi: \n")

print("capitalize() ->", complex.capitalize()) # First character in Uppercase
print("upper() ->",complex.upper()) # All characters in Uppercase
print("lower() ->",complex.lower()) # All characters in Lowecase
print("swapcase() ->",complex.swapcase()) # Uppercase in lowecase and reverse
print("title() ->",complex.title()) # The first letter of every word will be in Uppercase
print("count('character') ->", complex.count("a")) # Returns the count of the letter in the string
print("count('character', init,finish) ->", complex.count("a", 2, 5)) # Returns the count of the letter in the string
print("find('character') ->", complex.find("comp")) # Returns position
print("startswith('character') ->", complex.startswith("p")) # Returns boolean
print("startswith('character', position) ->", complex.startswith("comp", 0)) # Returns position
print("replace('character', 'character') ->", complex.replace("comp", "delta")) # Returns string
print("strip()->", complex.strip()) # Deletes space characters
print("strip('character')->", complex.strip("a")) # Deletes characters
print("split('character')->", complex.split(" ")) # Split in a new array a string
print("splitlines('character')->", complex.splitlines(complex+"\n line2 \n line 3 \n line4")) # Split in a new array a string
