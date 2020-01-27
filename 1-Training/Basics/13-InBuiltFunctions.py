#In-BuiltFunctions:

#Absolute value:
abs(-67) #67
abs(67) #67

#Boolean values:
bool(0) #False
bool(1) #True
bool(1000) #True
bool(None) #False

#Dir function: tell us all the possibility functions that I can use with the spsecific object or datatype:
dir("hello") #swapcase, title, spitlines, startswith, ... alll functions to manipulate the string type variable

#Help function:
sent="Pepito"
help(sent.upper)

#Eval function: takes a string and evaluate as a python code: 1 line
example = 'print("Eval Hi")'
eval(example)
#Exec function: > 1 line
exec(example)

#Conver into different datatypes:
a = '1'
print(str(1)) #'1'
print(int(a)) #1
print(float(a)) #1.0