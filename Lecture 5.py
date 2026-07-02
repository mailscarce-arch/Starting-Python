#Loop Structure
# two types of loops 1st While loops and 2nd for loops

# while loops
# i = 1
# while i <= 10 :
#     print("Hello World")
#     i += 1
 
# print(i)

#print numbers from 1 to 5

# i = 1
# while i<=5 :
#     print(i)
#     i += 1

# print("Loop Ended")

# i = 5
# while i>=1 :
#     print(i)
#     i -= 1

# print("Loop Ended")

#Practice Questions
#1 Print numbers from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i+=1
# print("loop Ended")


#2 Print numbers from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i-=1
# print("loop Ended")


#3 Print the multiplication table of a number n.
# n = int(input("Enter a number:"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i+=1
# print("Loop Ended")


#4 Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i <= 9:
#     print(num[i])   #what if the list is very large? that's why we use len(list)-1 
#     i += 1

# print("Loop Ended")

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i <= (len(num)-1):
#     print(num[i])   #what if the list is very large? that's why we use len(list)-1 
#     i += 1

# print("Loop Ended")


# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < (len(num)):
#     print(num[i])   #what if the list is very large? that's why we use len(list)-1 
#     i += 1

# print("Loop Ended")


#5 Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

# x = 81
# i = 0
# while i < (len(tup)):
#     if(tup[i] == x):
#         print("Found at index", i)
#     i += 1

# print("Loop Ended")


#Break and Continue Keyword
#Break
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

# x = 9
# i = 0
# while i < (len(tup)):
#     if(tup[i] == x):
#         print("Found at index", i)
#         break
#     else:
#         print("finding...")
#     i += 1

# print("Loop Ended")

#Continue

# i = 0
# while i <= 10:
#     if( i == 5):
#          i += 1
#          continue #Skip
#     print(i)
#     i += 1

# print("Loop Ended")

# i = 1
# while i <= 10:
#     if( i%2 != 0):    #not equal to !=
#          i += 1
#          continue #Skip
#     print(i)
#     i += 1

# print("Loop Ended")






#For Loop
# nums = [1, 2, 3, 4, 5, 6]
# for val in nums:
#     print(val)


#Practice Questions
#1st  Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for val in list:
#     print(val)



#2nd Search for a number x in this tuple using loop: 
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x = 16
# idx = 0
# for el in tup:
#     if(el == x):
#         print("number found at idx", idx)
#     idx += 1
        


#Range Function
# seq = range(5)
# for i in seq:
#     print(i)


# for i in range(5):  #range(stop)  only stop condition
#         print(i)


# for i in range(2, 5):  #range(start, stop)  start and stop condition
#         print(i)

# for i in range(2, 10, 2):  #range(start, stop, step)  start, stop and step condition
#         print(i)



# Practice Question
#1st print numbers from 1 to 100
# for i in range(101):
#         print(i)



#2nd print numbers from 100 to 1
# for i in range(100, 0, -1):
#     print(i)
        

#3rd print the multiplication table of number n.

# n = int(input("Enter a number:"))

# for i in range(1, 11):
#     print(n*i)  

#4th WAP to find the sum of first n numbers. (using while)

#while loop
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
    
# print("total number of sum=", sum)

#for loop  
# n = 5
# sum = 0
# for i in range (1, n+1):
#     sum += i

# print("total sum =", sum)


#5th WAP to find the factorial of first n numbers. (Using For)

#While loop
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
    
# print("factorial of n=", fact)

#For loop
# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print("factorial of n=", fact)




# #Past Statement
# for i in range(5):
#     pass
# print ("work")
