"""
String Exercises:
"""
# Exercise A:
string_a = input("Insert the string_a:")
string_b = input("Insert the string_b:")
if string_a.startswith(string_b):
    print(string_a, " starts with ", string_b)
else:
    print(string_a, " does not start with ", string_b)

# Exercise B:
while True:
    character_to_count = input("Insert the character to count: ")
    if len(character_to_count) == 1:
        break
print("Number of times ", character_to_count, " appears in ", string_a, " are: ", string_a.count(character_to_count))


