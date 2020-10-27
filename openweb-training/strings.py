simple = 'Simple string'
simpleII = "Simple string"
complex = '''
Complex string
'''

concat = simple + simpleII
print(concat)
index = simple[3]
print(index)
repetition = concat*3
print(repetition)
print(len(index))

# UNICODE character comparison:
print("a" > "A")