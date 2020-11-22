"""
Calculator
"""
number_a = int(input("Please introduce the first number: "))
print(f"The number {str(number_a)} was introduced")
number_b = int(input("Please introduce the first number: "))
print(f"The number {str(number_b)} was introduced")

print("Calculator:")
print(f"The addition is: {str(number_a + number_b)}")
print(f"The subtraction is: {str(number_a - number_b)}")
print(f"The product is: {str(number_a * number_b)}")
if number_b == 0:
    print(f"The division is: undefined")
else:
    print(f"The division is: {str(number_a / number_b)}")