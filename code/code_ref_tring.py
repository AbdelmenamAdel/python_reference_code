
#!============================= check the adminstration in a web page ==============================
# admins= ["Mohammed", "Ali", "Hassan", "Khalid","Abdo"]
# name=input("Enter your name: ").strip().capitalize()
# if name in admins:
#     print(f"Hello {name}, welcome back")
#     option=input("Would you like to update or delete your account? (D/U): ").strip().capitalize()
#     if option=="U" or option=="Update":
#         new_name=input("Enter new name: ").strip().capitalize()
#         admins[admins.index(name)]=new_name
#         print(admins)
#     elif option=="D" or option=="Delete":
#         admins.remove(name)
#         print(admins)
# else:
#     state=input("You are not an admin. Would you like to become one? (Y/N): ").strip().capitalize()
#     if state=="Y" or state=="Yes":
#         admins.append(name)
#         print("you have been added")
#         print(admins)
#     else:
#         print("you aren't added")
#!============================= Loop example ==============================
# people ={"mohammed": {"phone": "555-555-5555", "address": "123 Main St.","email": "mohammed@gmail.com",},
#           "abdo": {"phone": "555-555-5555", "address": "123 Main St.","email": "abdo@gmail.com",},
#           "sara": {"phone": "555-555-5555", "address": "123 Main St.","email": "sara@gmail.com",},
#          }
# for name in people:
#     print(f"\nDetails for: {name.center(20,'-')}")    
#     for info in people[name]:
#         print(f"{info} is: {people[name][info]}")
# else :
#     print("\nEnd of loop\n".center(40,'*'))
#!============================= Modules (pyfiglet and termcolor) ==============================
# import pyfiglet
# import termcolor

# print(dir(pyfiglet))

# ascii_banner = termcolor.colored(pyfiglet.figlet_format("Abdelmoneim"), color="red", attrs=["bold"])
# print(ascii_banner)

#!============================= Modules (datetime) datetime and time ===============================
# import datetime as dt
# print(f"the current year is : {dt.datetime.now().year}")
# print(f"the current mounth is : {dt.datetime.now().month}")
# print(f"the current day is : {dt.datetime.now().day}")
# print("@"*50)
# print(f"the current hour is : {dt.datetime.now().time().hour}")
# print(f"the current minute is : {dt.datetime.now().time().minute}")
# print(f"the current second is : {dt.datetime.now().time().second}")
# print("@"*50)
# ? Calculating time left for my birthday & Formatting date and time
# mybirthday = dt.datetime(year=2005, month=1, day=29)
# dateNow = dt.datetime.now()
# print(f"the time left for my birthday is : {(dateNow - mybirthday).days} days")
# ? Formatting date and time website   ###########   https://strftime.org/
# print(mybirthday.strftime("%A %d %b, %Y"))
# print(dateNow.strftime("%A %d %b, %Y"))
#!============================= Modules (Time) Decoration and SpeedTest ===============================
# from time import time
# def speedtest(func):
#     def nestedFun():
#         start = time()
#         func()
#         end = time()
#         print(f"the function {func.__name__} took {end - start} seconds")
#     return nestedFun

# @speedtest
# def loop():
#     for i in range(5000):
#         print(i)
# loop()
#!============================= OOP example 1 ===============================
# class MyClass:
#     x=5 #! Class variable 
#     def __init__(self,name,age,level):
#         self.name=name        #! Instance variable 
#         self.age=age          #! Instance variable 
#         self.level=level      #! Instance variable 

#     def __str__(self):
#         return f"my name is {self.name} and my age is {self.age} and my level is {self.level}"

# obj=MyClass("Abdelmoneim",20,10)
# print(obj)
#!============================= OOP example 2 Member ===============================
# class Member:
#     not_allowed_members=["Shit","Hell","Baloot"]  #! Static / Class variable
#     user_num=0                                    #! Static / Class variable
#     def __init__(self,fname,mname,lname,gender):  #! Constructor
#         self.fname=fname                          #! Instance variable
#         self.mname=mname                          #! Instance variable
#         self.lname=lname                          #! Instance variable
#         self.gender=gender                        #! Instance variable
#         Member.user_num+=1 
#     @classmethod                                  #! Class method
#     def show_users_count(cls):
#         print(f"We have {cls.user_num} users in our system.")
#     @staticmethod                                 #! Static method
#     def say_hello():
#         print("Hello from static method")
#     def __str__(self):                            #! Magic method
#         return f"My name is {self.fname} and my gender is {self.gender}"
#     def full_name(self):                          #! Normal method
#         if(self.fname in Member.not_allowed_members):
#             raise ValueError("This name is not allowed")
#         else :
#             return f"{self.fname} {self.mname} {self.lname}"
#     def name_with_title(self):                     #! Normal method
#         if(self.gender=="Male"):
#             return f"Hello Mr. {self.fname}"
#         elif(self.gender=="Female"):
#             return f"Hello Mrs. {self.fname}"
#         else :
#             return f"Hello {self.fname}"
#     def get_all_info(self):                        #! Normal method
#         return f"{self.name_with_title()}, Your full name is {self.full_name()}"
#     def delete_user(self):                         #! Normal method
#         Member.user_num-=1
#         print(f"{self.fname} is deleted")
# print(Member.user_num) 
# obj1=Member("Abdelmoneim","Adel","Abdelmoneim","Male")
# obj2=Member("Mohamed","Adel","Abdelmoneim","Male")
# obj3=Member("Basmala","Adel","Abdelmoneim","Female")
# obj4=Member("Sara","Adel","Abdelmoneim","Female")
# obj5=Member("Khalid","Adel","Abdelmoneim","Male")
# obj6=Member("Hassan","Adel","Abdelmoneim","Male")
# print(Member.user_num)
# obj5.delete_user()
# print(obj4.__str__())
# Member.show_users_count()
# print(obj1.get_all_info())
# print("@"*30)
# print(obj2.get_all_info())
# Member.say_hello()
# Member.show_users_count()
# print(Member.user_num)
#!============================= OOP example 3 Inheritance and Overriding ===============================
# class Car:                                #! Parent class
#     def __init__(self,brand,model,year):  #! Constructor
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def __str__(self):                    #! Magic method
#         return f"{self.brand} {self.model} {self.year}"
#     def power(self):
#         print(f"Works with petrol")
# class BMW(Car):                            #! Child class
#     def __init__(self,brand,model,year,engine,price):
#         self.engine=engine
#         self.price=price
#         super().__init__(brand,model,year)  #! Inheritance 
#     def __str__(self):
#         return f"Your BMW Info : \nBrand : {self.brand} \nModel : {self.model} \nYear : {self.year} \nEngine : {self.engine} \nPrice : {self.price}"
#     def power(self):                         #! Overriding
#         print(f"Works with diesel")          #! becaiuse of the same name of function in parent class it became overrided
    
# obj=BMW("BMW","X5","2024","V8",7000000)
# print(obj.__str__())
# obj.power()
#!============================= OOP example 4 Multiple Inheritance and Polymorphism ===============================
# class A:                                    #! Parent class
#     def do_something(self):                 #! Main method
#         print("I am A class") 
#         raise NotImplementedError("Drived class must implement this method")
# class B(A):                                #! Child class ( Single Inheritance )
#     def do_something(self):                #! Overrided method ( with another form )
#         print("I am B class")
# class C(A):                                #! Child class ( Single Inheritance )
#       def do_something(self):                #! Overrided method ( with another form )
#         print("I am C class")
# class D(B,C):                              #! Child class ( Multiple Inheritance )
#     def do_something(self):                #! Overrided method ( with another form)
#         print("I am D class")
    
# obj1=D()
# obj1.do_something()
