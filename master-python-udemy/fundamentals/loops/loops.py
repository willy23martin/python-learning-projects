"""
Loops:
"""

# For loop:
counter = 1
number = 90
for counter in range(1,20):
    number = counter * number
    print(f"The number was increased to: {number}")
    if number > 1000:
        break
else:
    print("Finished.")