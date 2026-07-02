# Functions

# #Function defination
# def calc_sum (a, b):  #Parameters
#     sum = a+b
#     print(sum)
#     return sum

# # 16 lines of codes

# calc_sum(15, 20)  #Function Call ; a and b is Arguments


# def print_hello():
#     print("Hello")

# print_hello()

#Create a function to calculte the average of 3 numbers

# def avg_num(a, b, c):
#     sum = a+b+c
#     avg = sum / 3
#     print(avg)
#     return avg


# # # 16 lines of codes

# avg_num(10, 50, 10)

#Practice Questions
#1st WAF to print the length of a list. (list is the parameter)

# cities = ["varanasi", "delhi", "mumbai", "surat"]


# def cal_list(list):
#     print(len(list))


# cal_list(cities)



#2nd WAF to print the elements of a list in a single line. (list is the parameter)

# cities = ["varanasi", "delhi", "mumbai", "surat"]

# def ele_list(list):
#     for item in list:
#         print(item, end=" ")


# ele_list(cities)



#3rd WAF to find the factorial of n. (n is the parameter)

# def cal_fact(n):
#     fact=1
#     i=1
#     while i <= n:
#         fact *= i
#         i += 1
#     print(fact)


# cal_fact(10)



# def cal_fact(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact *= i
#     print(fact)


# cal_fact(15)


#4th WAF to convert USD to INR.

# def converter(usd_val):
#     inr = usd_val * 96
#     print(usd_val, "USD=", inr, "INR")


# converter(100)


#5th WAF to take an input n and if the number is odd it should return ODD and if it's even it should return even

# def num(n):
#     if n%2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")


# num(76)


#Recursion
# recursive Function

# def show(n):
#     if n == 0:   #Base case
#         return
#     print(n)
#     show (n-1)

# show(5)

#reccurance 

# def fact(n):
#     if (n ==1 or n ==0):
#         return 1
#     return fact(n-1)*n
    

# print(fact(5))

#1st Write a recursive function to calculate the sum of first n natural numbers.

# def cal_num(n):
#     if(n == 0):
#         return 0
#     return cal_num(n-1) + n

# sum = cal_num(5)
# print(sum)
    



#2nd Write a recursive function to print all elements in a list. (Hint: use list & index as parameters.)

def ele_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    ele_list(list, idx+1)

num = [1, 2, 3, 4]

ele_list(num)







