# Lists: comma separated value that allow us to access items using indexes.

shopList = ["Apples", "Oranges", "Bananas", "Cheese"]
shopList[0] #"Apples"
shopList[0:2] #"Apples", "Oranges"

# Add elements to a list: append function
shopList.append("Blueberries")
# Edit elements
shopList[0] = "Cherries" #Replaces "Apples" by "Cherries"
# Delete an element
del shopList[2] # Deletes "Bananas"

#Append list to a list:
shopList2 = ["Apples", "Pineapples", "Bread"]
shopList + shopList2 # Append the second list to the firstone
# List length
len(shopList+shopList2)
# Duplicar the list:
shopList2 * 2

#Number list: maximum and minimum:
list = [1,2,1,75,45,-6]
max(list) #75
min(list) #-6
abs(min(list)) #6