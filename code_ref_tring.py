
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
#!============================= Modules pyfiglet and termcolor ==============================
# import pyfiglet
# import termcolor

# print(dir(pyfiglet))

# ascii_banner = termcolor.colored(pyfiglet.figlet_format("Abdelmoneim"), color="red", attrs=["bold"])
# print(ascii_banner)

#!============================= Modules datetime and time ===============================
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
#!============================= Decoration and SpeedTest ===============================
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
#!=============================  ===============================
