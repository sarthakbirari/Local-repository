#Creating a Dictionary
a={1:"one",2:"two"} 
print(a)

#Accessing Dictionary Element - Using Key and not Position
# a[1]
# Accessing Dictionary Element - Using Key and not Position
# a[0]


# Updating Dictionary
print(a)
a[1]="ONE" 
print(a)

# Add Element
a[3]="three"
print(a)
a[5]="four"
print(a)


# membership
1 in a

4 in a

3 not in a

# Copy - Dictionary is copied into another dictionary
print(a)
b=a.copy() 
print(b)


# Return a new view of the dictionary's items. It displays a list of dictionary’s (key, value) tuple pairs. 
a.items()

#displays list of keys in a dictionary
a.keys()

#displays list of values in dictionary
a.values()

#Remove the element with key and return its value from the dictionary
a.pop(5)

a.pop(1)
print(a)

# setdefault() - If key is in the dictionary, return its value. If key is not present, insert key with a value of dictionary and return dictionary
# When to Use setdefault()?
# When you want to fetch a value but ensure a key exists if it's missing.
# When working with collections (like lists or sets) in dictionaries to avoid KeyError.


dict1={1:"one",
       2:"two"}
print(a)
dict1.setdefault(3,"three")
print(dict1)


student = {"name": "Alice", "age": 21}
print(student.setdefault("age", 25))  # Output: 21 (does not change)
print(student)  


student = {"name": "Alice", "age": 21}
print(student.setdefault("grade", "A"))  # Output: A (inserts 'grade': 'A')
print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}


#setdefault() to initilaize the list
scores = {}
scores.setdefault("math", []).append(90)
scores.setdefault("science", []).append(85)
print(scores)  # Output: {'math': [90], 'science': [85]}


#It will add the dictionary with the existing dictionary
print(a)
b={4:"four"} 
a.update(b) 
print(a)



#It creates a dictionary from key and values
key={"apple","ball"} 
value="for kids" 
d=dict.fromkeys(key,value) 
print(d)

#length
print(a)
c=len(a)
print(c)

#clear()
print(a)
a.clear()
print(a)

# deleting the whole dictionary
a={1:"one",2:"two"} 
print(a)
del(a)
# print(a)

# 2. A company wants to keep track of its employees' departments using a dictionary. 
# The keys in the dictionary represent employee IDs, and the values represent the department names. 
# Write a Python program to:
# 1. Add a new employee to the dictionary.
# 2. Remove an employee from the dictionary.
# 3.  Find the department of a given employee ID.
# 4. List all employees in a specific department.


