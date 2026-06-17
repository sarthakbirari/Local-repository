# Nested tuple
# q1 and 2
nested_tuple=((10,20,30,40),("x","y","z"),(1.1,2.2,3.3,4.4,5.5))
print(nested_tuple[0][-2:])
print(nested_tuple[2][::2])

# q3
result=[]
for val in nested_tuple:
    result.append(val[-2:])
res=tuple(result)
print(res)


# q4
result=nested_tuple[1:][0][:-1]


# q5
nested_tuple=((10,20,30,40),("x","y","z"),(1.1,2.2,3.3,4.4,5.5))
print(nested_tuple)
# accessing elements in a nested tuple - access the first tuple, acces the second element in the second tuple 

nested_tuple[0]
nested_tuple[1][1]
print("first tuple:",nested_tuple[0])
print("second element in second tuple:",nested_tuple[1][1])

#  comparing nested tuples

t1=((1,2),(3,4))
t2=((1,2),(3,5))
print("t1==t2:",t1==t2)
print("t1<t2:",t1<t2)

# searching in a nested tuple
nested_tuple=((10,(20,30),40),("x","y","z"),(1.1,2.2,3.3,4.4))
search="y"
found = False 
for ele in nested_tuple: 
    if search_value in sub: 
        found = True 
        break 
print(search,"is found?:",found)

# reversing a nested tuple
nested_tuple=((10,(20,30),40),("x","y","z"),(1.1,2.2,3.3,4.4))
reversed_tuple=tuple(reversed (nested_nested))
print("reversed nested tuple:",reverseed-tuple)
