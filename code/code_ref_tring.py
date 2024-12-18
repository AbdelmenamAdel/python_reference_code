
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
#!============================= wep scraping (selenium) ===============================
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()

# driver.get('https://elzero.org')
# # ! I couldn't get it to work
# # element = driver.find_element_by_css_selector(".search-form").send_keys('Flutter')
# # element.send_keys('WebDriver')
# # element.submit()

# time.sleep(500)
# # driver.quit()
#!============================= NumPy Package ===============================
# ? multidimentional array [Matrix] not only on dimention
# import numpy as np
# my_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(my_array)
# print(my_array[0][1])
# print(my_array[0,1])
# print(my_array.ndim)
# print(my_array.shape)
# ? Slicing of array
# import numpy as np
# my_array=np.array([["A","B","C","D","E"],["F","G","H","I","J"],["K","L","M","N","O"],["P","Q","R","S","T"],["U","V","W","X","Y"]])
# print(">>"*15)
# print(my_array)
# print(my_array.ndim)
# print(my_array.shape)
# print(my_array[1,1:4])
# print("--"*15)
# print(my_array[1:4,1:4])
# print("<<"*15)
# ? Compare the memory location of list and array
# import numpy as np
# my_list=[1,2,3,4,5]
# print(id(my_list[0]))
# print(id(my_list[1]))
# my_array=np.array([1,2,3,4,5])
# print(id(my_array[0]))  
# print(id(my_array[1]))
# ? Compare the type of list and array
# import numpy as np
# my_list=[1,2,True,"4",5.50]
# my_array=np.array([1,2,True,"4",5.50])
# print(type(my_list[0]))
# print(type(my_array[0]))
# ? Compare the performance of list and array
# import numpy as np
# import time as t
# elements=15000000
# list1=range(elements)
# list2=range(elements)
# start_time=t.time()
# list3=[x+y for x,y in zip(list1,list2)]
# print(t.time()-start_time)
# start_time=t.time()
# array1 = np.arange(elements)
# array2 = np.arange(elements)
# array3 = array1 + array2
# print(t.time()-start_time)
# ? Compare the  memory size of list and array
import numpy as np
import sys 
my_list=range(100)
print(sys.getsizeof(my_list[0]))
print(len(my_list))
print(f"Memory size of list is : {sys.getsizeof(my_list[0])*len(my_list)}")
my_array=np.arange(100)
print(my_array.itemsize)
print(my_array.size)
print(f"Memory size of array is : {my_array.itemsize*my_array.size}")
# ? Specify the type of array and change it 
# import numpy as np
# # * int or 'int' or 'i'
# # * float or 'float' or 'f'
# # * complex or 'complex' or 'c'
# # * bool or 'bool' or 'b'
# # * str or 'str' or 's'
# # ! f -> float32 , float -> float64 , i -> int32 , int ->64 ,etc.
# print(">"*30)
# my_array=np.array([1,2,3,4,5],dtype="int")
# print(my_array)
# print(my_array.dtype)
# print("-"*30)
# my_array=my_array.astype("f") # float32
# print(my_array)
# print(my_array.dtype)
# print("<"*30)
# ? Min , Max , Sum of array
# import numpy as np
# my_array=np.array([1,2,3,4,5])
# print(my_array)
# print(my_array.min())
# print(my_array.max())
# print(my_array.sum())
# ? Ravel of array ( 1D )
# ! ravel used to convert ND array to 1D array
# import numpy as np
# my_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(my_array)
# print(my_array.ndim)
# x=my_array.ravel()
# print(my_array.ravel())
# print(x.ndim)
# ? Shape and Reshape of array
# import numpy as np
# print(">>"*15)
# my_array=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(my_array)
# print(my_array.ndim)
# print(my_array.shape)
# print("--"*15)
# my_array=my_array.reshape(3,4)
# print(my_array)
# print(my_array.ndim)
# print(my_array.shape)
# print("--"*15)
# my_array=my_array.reshape(2,6)
# print(my_array)
# print(my_array.ndim)
# print(my_array.shape)
# print("<<"*15)
# ! Virtual Environment & Virtual Environment Wrappers (venv)
#!============================= NumPy For Normalization ===============================
# ? Normalization if you want to understand and going on Machine Learning
# import numpy as np
# import pandas as pd
# data = [
#     [15.123, 2, 10.4567, 7],
#     [3.789, 14, 0.001, 6],
#     [19, 16.2345, 20, 11.987],
#     [7, 11.111, 9.8765, 3],
#     [8, 18.654, 1.234, 15],
#     [12.3456, 5, 13.89, 8],
#     [4, 6.543, 17, 14.0012]
# ]
# # ? notice the data before data frame
# # print(data[0]) # ! [15.123, 2, 10.4567, 7]
# data = pd.DataFrame(data)
# # ! data frame not only to show the data in table
# # ! but also to do mathematical operation
# # ! it convert each row to column
# # ! so you must be careful when you use it
# # ! you should re shape it to the past shape
# # print(data)
# # ? notice the data after data frame
# # print(data[0]) # ! [15.123,3.789,19,7,8,12.3456,4]
# # print(data.shape) # ! (7,4)
# print("--"*15)

# def normalization(n):
#     scale =(data[n]-min(data[n]))/(max(data[n])-min(data[n]))
#     scale=np.array(scale)
#     return scale
# s_data=np.array([normalization(0),normalization(1),normalization(2),normalization(3)])
# # print(s_data)
# # print(s_data.shape)
# print("--"*15)
# s_data=s_data.reshape(7,4)
# print(s_data)
# print("--"*15)
# trans=s_data.T
# covariance=np.cov(trans)
# # print(covariance)
# eigval,eigvec=np.linalg.eig(covariance)
# # print(eigval)
# # print(eigvec)
# res=eigval[3]/sum(eigval)+eigval[2]/sum(eigval)+eigval[1]/sum(eigval)
# # # print(res)
# projected1 = np.array(s_data.dot(eigvec.T[1]))
# projected2 = np.array(s_data.dot(eigvec.T[2]))
# projected3 = np.array(s_data.dot(eigvec.T[3]))

# final = np.array([projected1,projected2,projected3]).reshape(7,3)
# print(final)
# print("--"*15)
#!============================= NumPy another way for Normalization ===============================
# ? Normalization using sklearn package
# from sklearn.decomposition import PCA
# dec = PCA(n_components=3)
# final=dec.fit_transform(s_data)
# print(final)
#!============================= Pandas Package ===============================
import pandas as pd
# weather_data=[
#     ("20/8/2024", 30, "Rainy", 6),
#     ("21/8/2024", 35, "Sunny", 7),
#     ("22/8/2024", 29, "Cloudy", 8),
#     ("23/8/2024", 31, "Rainy", 9),
#     ("24/8/2024", 34.4, "Sunny", 10)
# ]
# df=pd.DataFrame(data=weather_data,columns=["day","temp","event","wind"])
# print(df)
# weather_data={
#     "day":["20/8/2024","21/8/2024","22/8/2024","23/8/2024","24/8/2024"],
#     "temp":[30,35,29,31,34.4],
#     "event":["Rainy","Sunny","Cloudy","Rainy","Sunny"],
#     "wind":[6,7,8,9,10]
# }

# weather_data=[
#     {"day": "20/8/2024", "temp": 30, "event": "Rainy", "wind": 6},
#     {"day": "21/8/2024", "temp": 35, "event": "Sunny", "wind": 7},
#     {"day": "22/8/2024", "temp": 29, "event": "Cloudy", "wind": 8},
#     {"day": "23/8/2024", "temp": 31, "event": "Rainy", "wind": 9},
#     {"day": "24/8/2024", "temp": 34.4, "event": "Sunny", "wind": 10}
# ]
# df=pd.DataFrame(weather_data)
# print(df)
# weather_data=pd.read_excel( "excel/Book1.xlsx",sheet_name="Sheet1")
# print(weather_data)
