# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))

# f.close()


# f = open("demo.txt", "r")
# line2 = f.readline()
# print(line2)

# f.close()



# f = open("demo.txt", "a")
# f.write("\nI am learning. 005")

# f.close()

#with Syntax

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)


# with open("demo.txt", "w") as f:
#     f.write("new data")


#Delete file
# using os module

# import os
# os.remove("file path")



#Practice Questions

#1st Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/o\nusing Java\nI like programming in Java")


#2nd WAF that replace all occurrences of "java" with "python" in above file.
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)




#3rd Search if the word "learning" exists in the file or not.

# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")


#with function

# def check_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")

# check_word()


#3rd WAF to find in which line of the file does the word "learning"occur first.   Print -1 if word not found.

# def check_line():
#     word = "ds"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1


# print(check_line())




#4th From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if (int (val) %2==0):
            count += 1

print(count)

