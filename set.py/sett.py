# set is the collection of items of the unordered items.
# each element in the set must be unique and immutable. dict and list are mutable wa cn not store them in set

collection={1,2,3,4,5,6,"kajal "} #duplicate value ignored
print(collection.pop()) #random vslue popped
print(collection)
print(len(collection))

collections={}#empty dictinary
print(type(collections))

collect=set() #empty set
print(type(collect))


#add ,remove, clear, pop method

collect.add(1)
collect.add(2)

collect.add(("kajal","tiwari"))
#collect.add(["kaju ","tiwari"]) list are mutable
#collect.clear()
print(len(collect))


print(collect)

#union and intersection

print(collection.union(collect))
print(collection.intersection(collect))

