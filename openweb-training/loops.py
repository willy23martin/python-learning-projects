"""
Loops:
"""

# While:
print("While starts.")
counter = 10;
while counter > 0:  # All the stop conditions
    print("The number is: ", counter)
    counter -= 1
print("While ends.")

# Beak and continue:
print("While continue and break starts.")
odd = 1
while odd <= 20:
    if odd == 19:
        break
    if odd % 2 == 0:
        print("The odd: ", odd)
    odd += 1
    continue
print("While continue and break ends.")

# For Lopp:
print("For starts.")
for var in range(1,11):
    print("Number: ", var)
print("For ends.")

print("For starts.")
for number in range(20, 1, 2):
    print("Number II: ", number)
print("For ends.")

for num in range(1,6):
    for prod in range(1,11):
        res = "%d * %d = %d";
        print(res % (num, prod, num*prod))