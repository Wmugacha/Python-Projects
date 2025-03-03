#Create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessin values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
print(thisdict["brand"])

y = thisdict.get("year")
print(y)

k = thisdict.keys() #Returns a list of the keys
print(k)

v = thisdict.values() #Returns a list of the values
print(v)

i = thisdict.items() #Returns dict items as tuples in a list
print(i)

#Check if a Key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 #By refering to its key name
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) #Using the update method
print(thisdict)

#Adding new items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red" #Using a new index key
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) #using the update method

#Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #Removes the last item added
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"] #Can also delete dictionary completely
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #empties the dictionary
print(thisdict)

#Loop through a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict: #Print all key names one by one
  print(x)

for x in thisdict.keys():
  print(x)

for x in thisdict: #Print all values
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items(): #Loops through both values & keys
  print(x, y)

#Copy a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() #Method 1
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) #Method 2
print(mydict)

#Nested Ddictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#Access items in the nested dictionary
print(myfamily["child2"]["name"])

#Loop through a nested dict
for x, obj in myfamily.items():
    print(x)                    #Loops through the dict in myfamily
    
    for y in obj:               #Loops through the dict items
        print(y + ':', obj[y])