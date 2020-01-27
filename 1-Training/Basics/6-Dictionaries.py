# Dictionary: key-value pairs

#Set the dictionary:
students = {"Bob":12, "Rachel":13, "Entity":18} #key:value
#Get data from the dictionary:
students["Rachel"] #13
# Edit values:
students["Entity"] = 22 #Change the 18 to the 22
# Remove the key-value pairs
del students["Entity"] # Removes the "Entity" key and its value
# NOTE: do not repeate the keys in a Dictionary because it will return the lastone key´s value
students = {"Bob":12, "Bob":14, "Bob":16}
students["Bob"] #16