#Create a set
set1 = set(("apple", "mango", "grapes", "oranges",)) #Create a set
set2 = {1, 4, 6, 8, 0}
set3 = {"Drake", "Beyonce", "Kanye", "Ed Sheeran", "apple"}
set4 = {True, False}

print(set1)
print(set2)
print(set3)
print(set4)

#Get the length of a set
print(len(set1))

#Loop through a set
for x in set3:
    print(x)

#Check if value is present on not
print ("mango" in set1)
print("mango" not in set1)

#Add items
set1.add("citrus")
print(set1)

#Add sets(Works with lists, dictionaries & tuples)
set1.update(set2)
print(set1)

#Remove items(Pop method will remove a random item)
set1.remove("citrus") #will raise error if item does not exist
set1.discard("oranges") #will not raise an error if it does not exit
print(set1)

#Clear/delete the set
#set1.clear()
print(set1)
#del set1 [Deletes the set completely]

#Join sets
set5 = set2.union(set3, set4) #Works with tuples as well
set6 = set2 | set3 | set4 #Only with sets
print(set5)
print(set6)

set5.update(set6) #Inserts items from one set into another
print(set5)

set7= set1.intersection(set3) #Returns a set with common items
print(set7)

set8 = set1 & set3 #Only with sets
print(set8)

set7.intersection_update(set8) #It will change the original set instead of returning a new set
print(set7)

set9 = set1.difference(set3) #will return a new set that will contain only the items from the first set that are not present in the other set.
set10 = set1 - set3 #only with sets
print(set9)
print("x")
print(set10)

set1.difference_update(set3) #will keep only the elements that are NOT present in both sets
print(set1)

set11 = {"apple", "banana", "cherry"}
set12 = {"google", "microsoft", "apple"}
set13 = set1.symmetric_difference(set2) #will keep only the elements that are NOT present in both sets
print(set13)