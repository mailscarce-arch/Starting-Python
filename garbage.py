# Q4. Simple addition

# Store two numbers in variables, add them, and print a sentence.

# Expected (example with 12 and 8):
# The sum of 12 and 8 is 20

# Q4 a = 12
# b = 8

# add = a+b
# print("The sum of 12 and 8 is", add)



# Q5. Simple multiplication with f-strings
# Store two numbers, multiply them, and print using an f-string this time.
# Expected (example with 6 and 7):
# 6 multiplied by 7 is 42

# a = 6
# b = 7
# multi = a*b
# print("a multiplied by b is", multi)


# Q6. User input

# Use the input() function to ask the user their name, then greet them.

# Expected (if user types Aryan):
# Hello, Aryan! Welcome.
# name = input("Enter Your Name :")
# print("Hello", name, "Welcome")



# Q7. Even or odd
# Take a number stored in a variable. Use if/else to print whether it's even or odd.
# Expected (example with 7):
# 7 is odd

# num = 7
# rem = num%2 
# if rem == 0:
#     print(num, "is Even")
# else:
#     print(num, "is Odd")




# Q8. Loop and print
# Use a for loop with range() to print numbers 1 to 5, each on its own line.
# Expected:
# 1
# 2
# 3
# 4
# 5

# for n in range(1, 6):
#     print(n)






# Q9. Multiplication table
# Use a for loop to print the multiplication table of a number from 1 to 10.
# Expected (example with number 5):
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

# num = int(input("Enter a number:"))
# i = 1
# for i in range(1, 11):
#         print(num,"X", i, "=", num*i)








# Q10. Sum of numbers in a list
# You have a list of numbers. Use a for loop to add them all up yourself — without using the sum() function — and print the total.
# pythonnumbers = [4, 8, 15, 16, 23, 42]
# Expected:
# Total: 108

# list = [4, 8, 15, 16, 23, 42]
# i = [0]
# for i in range([0], len(list)-1):
#     if i < len(list):
#         print(i+)
    

# numbers = [4, 8, 15, 16, 23, 42]
# total = 0          # a running total, starting at zero

# for num in numbers:   # loop directly over the list — no range() needed here
#     total = total + num    # add this number to the running total

# print("Total:", total)




# Q11. Counting with a condition
# From this list, count how many numbers are greater than 10. Use a loop and an if check, with a counter variable.
# pythonnumbers = [4, 8, 15, 16, 23, 42]
# Expected:
# Count: 3

list = [4, 8, 15, 16, 23, 42]
i = 0
for val in range(0, len(list)-1):
    if i>=10:
        print(i)
        i += 1


print(i)







# Q12. FizzBuzz (a famous beginner classic)
# Loop through numbers 1 to 15. For each number: if it's divisible by 3, print "Fizz". If divisible by 5, print "Buzz". If divisible by both 3 and 5, print "FizzBuzz". Otherwise, print the number itself.
# Expected (partial):
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz





# Q13. A simple function

# Write a function called square that takes a number and returns its square (number multiplied by itself). Then call it with the number 9 and print the result.

# Expected:
# 81