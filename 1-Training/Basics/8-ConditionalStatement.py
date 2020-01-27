#Conditional Statements:

# If-Conditional:
if(3.999 < 4):
    print("Condition is true")
else:
    print("Condition is not true")

# Conditional operators: >=, <=, ==, !=, >, <
# AND condition:
age = 16
if(age < 15):
    print("You are young")
elif(age >=15 and age<18):
    print("You are a teenager")
else:
    print("You are an adult")

# OR conditions:
if(age < 15):
    print("You are young")
elif(age >=15 or age<18):
    print("You are a teenager")
else:
    print("You are an adult")

