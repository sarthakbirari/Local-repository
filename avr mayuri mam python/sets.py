#Create a set my_set, which contains the elements 1 to 5. Create using both the syntax {} and set()
#  syntax {}
 
my_set = {1,2,3,4,5}
print(my_set)
set()
my_set = set([1, 2, 3, 4, 5])
print(my_set)

#Create a set my_set1 which contains the mixed type of elements 1, 2.5 and Python. Create using both the syntax
my_set={1,2.5,"python"}
print(my_set)
my_set1=([1,2.5,"python"])
print(my_set1)

#Create an empty set
s1 = set()
print(s1)

# Adds a single element - add()
s1.add(5)
print(s1)


# update() - Removes duplicate elements
# update() updates the set, and if any duplicate elements are present, it will be removed

set1 = {1, 2, 3,}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

# Removes 6 from set1 - remove()
# if the element is found, it will be removed otherwise, we will get key error
# set1.remove(6)
# print(set1)

# discard() - Removes 6 if present; does nothing if not found
set1.discard(6)
print(set1)

# pop() - Removes and returns an arbitrary element
set1.pop()
print(set1)


# union() - joins two sets
# Duplicate elements will be removed
set_union1={1,2,3}
set_union2={3,4,5}
union=set_union1.union(set_union2)
print(union)

#  Set Intersection - intersection() 
# Symmetric Difference - symmetric_difference()
# Set Difference - difference()

# Subset and Superset
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))
print(set2.issuperset(set1))

set1 = {1, 2, 5}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))
print(set2.issuperset(set1))

# Subset and Superset
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))
print(set2.issuperset(set1))

# Check Membership
set1 = {1, 2, 3, 4}
print(2 in set1)    
print(10 in set1)
print(2 not in set1)
print(10 not in set1)

#clearing a set

set1={1,2,3,4,}
print(set1.clear())

#Copying a set
s1={1,2,3,4,5}
print(s1)  #{1, 2, 3, 4, 5}
s2 = s1.copy()
print(s2)  #{1, 2, 3, 4, 5}


#length of the set
s1={1,2,3,4,5}
print(len(s1))


# isdisjoint()-Returns True if two sets have null intersection
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.isdisjoint(set2))

set1 = {5,6,7,8}
set2 = {1,2,3,4}
print(set1.isdisjoint(set2))

# all() - Returns True if all the elements are true 
set1 = {5,6,7,8}
print(all(set1))

set1 = {0,5,6,7,8}
print(all(set1))


# any() - Returns True if any of the elements are true
set1 = {5,6,7,8}
print(any(set1))
set1 = {0,5,6,7,8}
print(any(set1))

# max()
set1 = {0,5,6,7,8}
print(max(set1))

# min()
set1 = {0,5,6,7,8}
print(min(set1))



# sorted() - returns a new list, not a set.
my_set = {5, 1, 4, 3, 2}
sorted_list = sorted(my_set)
print("Sorted List:", sorted_list) 


# sum()
set1 = {1, 3, 5}
print(sum(set1))


# enumerate() - Returns an enumerate object that contains index and value of the set as a pair




# Sets in Python are unordered collections, so their elements don't have a fixed position.
my_set = {5, 1, 4, 3, 2}
print(my_set)
# When you print or access the set, the order may be different from how you defined it.
{1, 2, 3, 4, 5}




