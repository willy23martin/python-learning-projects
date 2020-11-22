"""
Exercises:
"""

# Receive country and continent as inputs and print them in the screen
print("Starting  1.")
country = input("Please insert your country:")
print(f"The country inserted was: {country} of type {type(country)}")
continent = input("Please insert your continent: ")
print(f"The continent inserted was: {continent} of type {type(continent)}")
print("Finish 1.")
print("################# \n")

# Even numbers between 1 and 100:
print("Starting  2.")
number = 0
for number in range(0, 101):
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")
print("Finish 2.")
print("################# \n")