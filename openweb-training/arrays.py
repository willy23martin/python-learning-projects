"""
Lists:
- Mutables
"""
array = []
print("Type: ", type(array), " - ",array)
array_sec = [1, "a", True]

# For in order to know about elements:
for el in array_sec:
    print("Elemento dell'elenco: ", el)

# zip:
array_list = [1,2,4,5]
zipped_array = zip(array_sec, array_list)
print("zip(list_a, list_b)->[pair elements]-> ", zipped_array)
for zipped_element in zipped_array:
    print("Zipped element-> ", zipped_element)

# Precedence:
print(5 in zipped_element)
print(5 in array_list)

print("Concat lists-> ", array_sec + array_list)
print("Position 3 -> ", array_list[3])
print("Lists -> ", array_list[2:4])
print("Max element ->", max(array_list))
print("Min element ->", min(array_list))
print("Sort elements ->", sorted(array_list))
print("Reverse sort elements ->", sorted(array_list, reverse=True))

# Table:
table = [[1,2,4], [0,0,0], [0,5,6]]
for row in table:
    for elem in row:
        print("Row element -> ", elem)

