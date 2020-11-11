"""
Alternatives:
"""

y = int(input("Insert a number"))
if y <= 18:
    print("Its true")
elif y > 18 and y <= 28:
    print("Its in the middle")
else:
    print("Its false")

# Exercise 2:
number = int(input("Please insert the number:"))
if number == 0:
    print("The number is equal to zero.")
elif number > 0:
    print("The number is grater than zero")
else:
    print("The number is negative")

# Exercise 5: user and password pepe and asdasd
user = input("Please insert your username:")
password = input("Please insert your password")
if user == "pepe" and password == "asdasd":
    print("It is correct")
else:
    print("It is not correct")

# Exercise 9: three numbers ordered asc:
numberA = int(input("Please insert the first number:"))
numberB = int(input("Please insert the second number:"))
numberC = int(input("Please insert the third number:"))
max_number = max(numberA, numberB, numberC)
if max_number == numberA:
    print("The numberA is the greatest")
elif max_number == numberB:
    print("The numberB is the greatest")
else:
    print("The numberC is the greatest")

# Exercise 13: Insert date (day, month, year) and if it is correct:
days_per_month = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

month = input("Please insert the name of the month:")
days = input("Please insert the number of days of the month")
if days_per_month[month] == days:
    print("It is ok")
else:
    print("It is not ok")