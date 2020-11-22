lower_limit = int(input("Please insert the lower limit: "))
upper_limit = int(input("Please insert the upper limit: "))
number = lower_limit
for number in range(lower_limit, upper_limit):
    print(f"The number {number} is between {lower_limit} and {upper_limit}")