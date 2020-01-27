# Functions:

def HelloWorld():
    print("Hello world")

HelloWorld()

#The parameter does not necessary be defined with its type
def Greeting(name):
    print("Hello: " + name + ":)")
Greeting("Pepito")

def Add(num1, num2):
    print("The addition is: ", num1+num2)
Add(10,15)

# Function with return value:
def ReturnAdd(num1, num2):
    return num1+num2
addition = ReturnAdd(56,8998)
print(addition)