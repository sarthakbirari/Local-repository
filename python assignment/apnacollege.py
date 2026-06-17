# APNA COLLEGE PYTHON PLAYLIST VIDEO 2

# slicing of string 
# sen="sarthak birari"
# len=len(sen)
# print(len)

# a=sen[1:15]
# print(a)

# PRACTICE QUESTION ON STRING
# name=input("enter the name")
# print(len(name))

# sen=("hi i am $ and you are also $ so can we be friends")
# print(sen.count("$"))


# CONDITIONAL STATEMENTS QUESTION PRACTICE 
# WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
# num=int(input("enter the number"))

# if(num % 2 == 0):
#     print("the number is even")
# else:
#     print("the number  is odd")   


# WAP TO FIND THE GREATEST OF 4 NUMBERS ENTERED BY THE USER
# a=int(input("enter the first number"))
# b=int(input("enter yhe second number"))
# c=int(input("enter the third number"))
# d=int(input("enter the fourth number"))

# if(a>=b and a>=c and a>=d):
#     print("a is the greatest number")
# elif(b>=c and b>=d):
#     print("b is the greatest number")
# elif(c>=d):
#     print("c is the greatest number")
# else:
#     print("d is the greatest number") 


# WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT
# num=int(input("enter the number"))
# if(num % 7 == 0):
#     print("the number is multiple of 7")
# else:
#     print("the number is not a multiple of 7")  




# LISTS AND TUPLE IN PYTHON VIDEO 3

# LISTS:
    
# list1=["sarthak",12,"ritika",10,"ganesh",40]
# print(list1)
# print(len(list1))
# print(list1[3])


# lists are mutable
# list2=[1,10,3,"krishna","radhe"]
# print(list2[0])
# list2[0]="sarthak"
# print(list2)

# LIST SLICING ( SIMILAR TO STRING SLICING )
# list3=[10,"water",19,"spoon","colour",3]
# print(len(list3))
# print(list3[1:5])
# negative list slicing
# list4=[1,"hello",4,30,"hi","fine"]
# print(list4[-5:-2])


# LIST METHODS

# list5=[2,5,7,1,4]
# list5.append(10) #adds one element at the end 
# print(list5)

# list5.sort() #sorts in ascending order  
# print(list5)

# list5.sort(reverse=True) #sorts in descending order 
# print(list5)

# list5.reverse() #reverses list  
# print(list5)

# list5.insert(1,3) #insert element at index
# print(list5)

# list6=[2,4,7,2,5]
# list6.remove(2) #removes first occurrence of element 
# print(list6)

# list7=[1,3,1,4,8,10]
# list7.pop(0) #removes element at index 
# print(list7)


# TUPLE: (tuples are immutable)


# tuple1=(1,3,7,9,10)
# print(tuple1)
# print(type(tuple1))
# print(len(tuple1))
# # indexing
# print(tuple1[1])

# if we have to to print a single element in tuple so give coma ( , ) in last for e.g.,
# tuple1=(1,) 

# TUPLE SLICING:

# tuple2=(1,5,7,10,11,15)
# print(tuple2[0:4])
# print(tuple2[0:6:2])

# # negative slicing

# tuple3=("a","b","r","v","t","e")
# print(tuple3[-6:-4])
# print(tuple3[-4:-1])

# # TUPLE METHODS:

# tuple4=(1,3,6,2,6,3,)
# print(tuple4.index(6)) #returns index of first occurence
# print(tuple4.index(2))

# tuple5=(2,5,2,6,7,6,8,6)
# print(tuple5.count(6)) #counts total occurremces

# # PRACTICE QUESTIONS 

# # WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVORITE MOVIES AND STORE THEM IN A LIST
# list=[]
# list1=input("enter the first name")
# list2=input("enter the second name")
# list3=input("enter the third name")
# list.append(list1)
# list.append(list2)
# list.append(list3)
# print(list)



# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS (HINT: USE COPY()METHOD)
# list1=["m","a","a","m"]

# list2=list1.copy()
# list1.reverse()
# if(list1==list2):
#     print("palindrome")
# else:
#     print("not palindrome")


# WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE
# ["C",'D","A","A","B","B","A"]

# tuple=("A","D","A","A","B","B",'A',)
# print(tuple.count("A"))


# # STORE THE ABOVE VALUES IN ALIST AMND SORT THEM FROM "A" TO "D"
# list=["A","D","C","B"]
# list.sort()
# print(list)



# DICTIONARY AND SET IN PYTHON VIDEO 4

# DICTIONARY:
# dictonaries are used to store data values in key:value pairs
# they are unordered, mutable(changeable) and dont allow duplicate keys 

# dict={"key" : "value",
#       "name" : "sarthak",
#       "subjects" : ["python","java","cpp"],
#       "age" : 18,
#       }
# print(dict["key"])
# print(dict["age"])
# print(dict["name"])

# dict["age"]=19
# dict["address"]="barwani"
# print(dict)

# NESTED DICTONARY

# dict1={"players" : ["virat kohli","rohit sharma","hardik pandya"],
#       "runs" : {
#           "virat kohli" : 100,
#            "rohit sharma" : 101,
#             "hardik pandya" : 51,
#             }
#  }
# print(dict1)
# print(dict1["runs"]["virat kohli"])
# print(len(dict1))
# print(list(dict1))


# # DICTONARY METHODS:

# dict2={"family_members" : ["sarthak","ritika","poonam","ganesh"],
#       "sarthak" : "student",
#       "ritika" : "student",
#       "poonam" : "nurse",
#       "ganesh" : "barber",
#       }

# print(dict2.keys()) #returns all keys
# print(list(dict2.keys()))


# print(dict2.values()) #returns all values 
# print(list(dict2.values( )))


# print(dict1.items()) #returns all key value pairs as tuple
# pairs=list(dict1.items())
# print(pairs[0])


# print(dict1.get("players")) #returns the key according to value


# dict3={"city" : "niwali"}
# dict1.update(dict3) #insert the specified items to the dictionaries 
# print(dict3)




# SETS:
# set is the collection of the unordered items 
# each element in the set must be unique and immutable
#repeated elements stored only once, so it resolved to {1,2}


# collection={1,2,3,10,1,10,"hello","hi"}
# print(collection)
# print(len(collection)) 
# print(type(collection))

# for empty set: collection = set() 


# SET METHODS:

# set1={1,2,"indore",10,"indore",12}
# set1.add(5) #adds an element
# print(set1)


# set1.remove(1) #removes an element
# print(set1)

# set1.clear() #empities the set
# print(set1)
# print(len(set1))

# set2={"sarthak","ritika","poonam","ganesh"}
# set2.pop() # removes a random values 
# print(set2)

# set3={1,2,3}
# set4={3,4,5}
# print(set3.union(set4)) #combines both set values and returns new 

# print(set3.intersection(set4)) #combines common values and returns new 




# PRACTICE QUESTIONS:

# STORE FOLLOWING MEANINGS IN A PYTHON DICTIONARY

# key_values={"table" : ("a piece of furniture","list of fac7t and figures"),
#             "cat" : "a small animal" }
# print(key_values)



# you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classroom are needed by all students. 

# # set={"python","java",
#      "cpp","js","c"}
# print(len(set))



# WAP TO ENTER MARKS OF 3 SUBJECTS FROM THE USERR AND STORE THEM IN A DICTONARY. START WITH AN EMPITY DICTONARY AND ADD ONE BY ONE. USE SUBJECT NAME AS KEY AND MARKS AS VALUE 

dict1={}
s1=input("enter the 1st subject")
s2=input("enter the 2nd subject")
s3=input("enter the 3rd subject")

dict1.update({s1:92})
dict1.update({s2:95})
dict1.update({s3:91})

print(dict1)



