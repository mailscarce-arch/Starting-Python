#Dictionary
# info = {
#     "key" : "value",
#     "name" : "Sam",
#     "learning" : "Coding"
# }

# print(info["key"])
# print(info["name"])
# print(info["learning"])

# print(info)

# info["name"] = "Samad"
# print(info)


#Nested Dictionary
# student = {
#     "name" : "Sam",
#     "Subjects and marks" : {
#         "physics" : 90,
#         "chem" : 80,
#         "maths" : 95
#     }
# }

# print(student)
# print(student["Subjects and marks"] ["chem"])


#Dictionary Methods
#1 myDict.keys
# student = {
#     "name" : "Sam",
#     "Subjects and marks" : {
#         "physics" : 90,
#         "chem" : 80,
#         "maths" : 95
#     }
# }

# print(student.keys())

# print(list(student.keys()))   #List type casting
# print(len(student))             #Length

# print(list(student.keys()))

#2 Values Method (myDict.values())
# student = {
#     "name" : "Sam",
#     "Subjects and marks" : {
#         "physics" : 90,
#         "chem" : 80,
#         "maths" : 95
#     }
# }

# print(student.values())

# print(list(student.values()))   #List type casting
# print(len(student))             #Length

# print(list(student.values()))

#3 mydict.items() (Items Method)
# student = {
#     "name" : "Sam",
#     "Subjects and marks" : {
#         "physics" : 90,
#         "chem" : 80,
#         "maths" : 95
#     }
# }

# # print(student.items())
# pairs = list(student.items())

# print(pairs[0])

#4 Get Method mydict.get("key") 
# student = {
#     "name" : "Sam",
#     "Subjects and marks" : {
#         "physics" : 90,
#         "chem" : 80,
#         "maths" : 95
#     }
# }
# print(student["name"])  #Don't use as it will bring error and rest of the codes won't execute
# print(student.get("name")) #it will return none if wrong but still the next code will be executed 

# Update Method mydict.update(newdict) 
# student = {
#     "name" : "Sam",
#     "Subjects and marks" : {
#         "physics" : 90,
#         "chem" : 80,
#         "maths" : 95
#     }
# }

# student.update({"city" : "vns"})

# new_dict = {"city" : "vns"}
# student.update(new_dict)

# print(student)



# Sets In Python
# collection = {1, 2, 3, 4, 4, 2, 3}
# print(collection)       #it ignores the duplicate values because in sets duplicate values are not allowed
# print(len(collection))

# collection = set()      #this is how we write empty set because {} is an empty dict syntax
# print(type(collection))

#Method of sets
#1 add method (set.add(ele))
# collection = set()
# collection.add(1)
# collection.add(2)

# print(collection)

#2 remove method (set.remove(ele))

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)

# print(collection)

# collection.remove(3)
# print(collection)

#3 clear method (set.clear())
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)

# print(collection)

# collection.clear()
# print(collection)

#3 pop method (set.pop())  it randomly removes some element one and more, not fixed which element
# collection = {"hello world", "Sam","Coding", "python"}

# print(collection.pop())


#3 union method (set.union(set2))
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))     #dosen't replace the orignal sets, it creates a new set returns
# print(set1)
# print(set2)

# #4 intersection method (set.intersection(set2)) returns a common value of set1 and set2
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.intersection(set2)) 


#Practice question
#1 Store following word meanings in a python dictionary :
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

# dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }

# print(dict)


#2 You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

# classroom = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(len(classroom))



#3 WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# marks = {}
# a = int(input("enter phy marks:"))
# marks.update({"phy" : a})

# b = int(input("enter chem marks:"))
# marks.update({"chem" : b})

# c = int(input("enter maths marks:"))
# marks.update({"maths" : c})

# print(marks)
# print(type(marks))



#4 Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
# values = {9, 9.0}
# print(values)       #it prints {9} because in python 9 and 9.0 is considered same that's why we use built-in data types or we can also store them as strings

# values = {
#     ("int", 9),
#     ("floating", 9.0)
# }

# print(values)
