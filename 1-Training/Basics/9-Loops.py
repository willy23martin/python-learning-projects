# Loops:
#for Loop: iterates thorough the list iten by item.
tup1 = (13,12,15)
list1 = ["Apples", "Bananas", "Cherries"]
for item in list1:
    print(item)
for t in tup1:
    print(t)
# Ranges:
for i in range(0,10): #number range from 0 to 9
    print(i) # 0,1,2,3,4,5,6,7,8,9
# Ranges with skipping:
for i in range(0,11,2): #number range from 0 to 9
    print(i) # 0,2,4,6,8,10

#Nested For Loops:
for i in range(0,5):
    for j in range(2,4):
        print(i+j)
#======================

# While Lopps:
c=0
while c < 5:
    print(c)
    c = c + 1
    if c < 3: continue
    else: break

#Wile with force passing:
c=0
while c < 5:
    print(c)
    c = c + 1
    if c == 3: pass
