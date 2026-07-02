# Class and objects

# class car:
#     color = "Blue"
#     brand = "BMW"
#     Model = "M4 competition"          #its a class

# car1 = car()
# print(car1.color)
# print(car1.brand)
# print(car1.Model)                     #it's an object


# Constructor __init__function
# class student:
#     def __init__():
#         print("Adding new student in database")
#     name = "karan"

# s1 = student()
# print(s1.name)

# s2 = student()
# print(s1.name)


class student:
    def __init__(self, Fullname):
        self.name = Fullname
        print("Adding new student in database..")

s1 = student("karan")
print(s1.name)
