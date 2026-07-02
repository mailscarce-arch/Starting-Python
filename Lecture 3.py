# List 
# marks = 95
# marks = 90
# marks = 85
# marks = 70

# # Instead we can write this way
# marks = [95, 90, 85, 70]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(len(marks))

# student = ["karan", 95, 18, "delhi"]
# print(student[0])
# student[0] = "Arjun"

# print(student[0])

# # List slicing
# marks = [50, 20, 60, 90, 70]
# print(marks[1:4])  #also have negative indexing

# List Method
# #1st appending method
# list = [2, 1, 3]
# list.append(4)
# print(list) #add elements in the last

#2nd (Sorting method)
# list = [5, 4, 6, 7, 52, 57, 16]
# list.sort()
# print(list)

# list = [5, 4, 6, 7, 52, 57, 16]
# list.append(4)
# list.sort()
# print(list)

# list = [5, 4, 6, 7, 52, 57, 16]
# list.append(4)
# list.sort(reverse=True)
# # print(list)
# list = ["apple", "mango", "litchi", "banana"]
# # list.append(4)
# list.sort(reverse=True)
# print(list)

#Reverse List
# list = ["a", "b", "C", "D"]
# list.reverse()
# print(list)

# #Insert method
# list = [50, 40, 60, 90,]
# list.insert(2,85)
# print(list)

# #remove method
# list = [50, 40, 60, 90,]
# list.remove(60)
# print(list)

# #pop method
# list = [50, 40, 60, 90,]
# list.pop(2)
# print(list)

#Tupples

# tup = (50, 40, 60, 90,)
# print(type(tup))

# tup = (1,)              #must have comma in last for single tupple
# print(type(tup))
# tup = (50, 40, 60, 90,)
# print(tup[1:4])

#Tuple Methods
# #1st Index Method
# tup = (50, 40, 60, 90,)
# print(tup.index(40))

#2st count Method
# tup = (50, 40, 60, 40, 90, 40,)
# print(tup.count(40))

# Practice Test
# 1st WAP to ask the user to enter the name of their 3 favorite movies and store them in a list 
# first = (input("Enter the first movie name:"))
# Second = (input("Enter the Second movie name:"))
# Third = (input("Enter the Third movie name:"))
# print([first, Second, Third])

# Another way
# movies = []
# first = (input("Enter the first movie name:"))
# Second = (input("Enter the Second movie name:"))
# Third = (input("Enter the Third movie name:"))

# movies.append(first) 
# movies.append(Second) 
# movies.append(Third) 

# print(movies)

# Another way
# movies = []
# movies.append(input("Enter the first movie name:"))
# movies.append(input("Enter the Second movie name:"))
# movies.append(input("Enter the Third movie name:"))

# print(movies)

# 2nd WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# list1 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("not Palindrome")


# list2 = [1, 2, 1]

# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#     print("Palindrome")
# else:
#     print("not Palindrome")


# list2 = ["m", "a", "a", "m"]

# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#     print("Palindrome")
# else:
#     print("not Palindrome")

# 3rd WAP to count the number of students with the "A" grade in the following tuple. ["C", "D", "A", "A", "B", "B", "A"]

# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))


# Store the above values in a list & sort them from "A" to "D"
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)

# grade = ["C", "D", "A", "A", "B", "B", "A"]
# print(grade.sort())

# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)







