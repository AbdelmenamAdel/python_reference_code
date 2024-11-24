
# # # ! quiz 1
# # for i in range(1, 101):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print("FizzBuzz")
# #     elif i % 3 == 0:
# #         print("Fizz")
# #     elif i % 5 == 0:
# #         print("Buzz")
# #     else:
# #         print(i)
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # #   ! quiz 2
# # from math import PI
# # def area_of_circle(radius):
# #     return PI * radius**2
# # radius = float(input("Enter the radius of the circle: "))
# # area = area_of_circle(radius)
# # print("The area of the circle is: ", area)
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # #   ! quiz 3
# # def primeORnot(num):
# #     if num > 1:
# #         for i in range(2, int(num ** 0.5) + 1):
# #             if (num % i) == 0:
# #                 return False
# #         return True
# #     else:
# #         return False

# # def prime_from_1_to_100():
# #     primes = []
# #     for i in range(1, 101):
# #         if primeORnot(i):
# #             primes.append(i)
# #     return primes

# # # Get the list of primes
# # primes = prime_from_1_to_100()
# # print(primes)

# # # Create a dictionary with primes and their squares
# # pc_dict = {i: i**2 for i in primes}
# # print(pc_dict)

# # ?????????????????????????????????????????????????????????????????
# # *--------------------  Uniform Search Cost  ---------------------
# def path_cost(path):
#     path_cost = 0
#     for (node, cost) in path:
#         path_cost += cost
#     return path_cost,path[-1][0]
# def USC(graph ,start,goal ):
#     visited=[]
#     queue=[[(start,0)]]
#     while queue:
#         queue.sort(key=path_cost)
#         path=queue.pop(0)
#         node=path[-1][0]
#         if node in visited:
#             continue
#         visited.append(node)
#         if node is goal:
#             return path
#         else:
#             for (node, cost) in graph.get(node, []):
#                 new_path=path.copy()
#                 new_path.append((node,cost))
#                 queue.append(new_path)

# graph = {
#     "S":[("A",2),("B",3),("D",5)],
#     "C":[("G",2),("D",1)],
#     "A":[("C",4)],
#     "D":[("G",5)],
#     "B":[("D",4)],
#     "G":[]
# }
# solution_path=USC(graph,"S","G")
# print("Solution is ",solution_path)
# print("The whole solution time is ",path_cost(solution_path)[0])


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# class Car:
#     def __init__(self,  color,mileage):
#         self.mileage = mileage
#         self.color = color
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage} miles."
#     def display_info(self):
#         return f"The {self.color} car has {self.mileage} miles."
# c1=Car( "blue",20_000)
# c2=Car("red",30000)
# print(c1)
# print(c2)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#             return f"The {self.name} dog is {self.age} years old."
#     def speak(self,sound):
#             return f"{self.name} says {sound}."
# class GoldenRetriver(Dog):
#       def speak(self,sound):
#           return super().speak(sound)


# dog1 = Dog("Fido", 3)
# print(dog1.speak("Woof"))


# print(dog1)

# dog2 = GoldenRetriver("Buddy", 5)
# print(dog2)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# create a series of the top 5 most populous countries with their populations
# import pandas as pd

# data = {
#     "Country": ["China", "India", "United States", "Indonesia", "Brazil"],
#     "Population": [142_000_000, 1_400_000_000, 329_000_000, 270_000_000, 210_000_000]
# }

# df = pd.DataFrame(data)

# top_5_countries = df.nlargest(5, "Population")

# print(top_5_countries)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# creating infrormation about 5 products(product name ,price,stock) and calculate the avarage of the prices
# import pandas as pd

# data = {
#     "Product Name": ["Product A", "Product B", "Product C", "Product D", "Product E"],
#     "Price": [100, 200, 150, 250, 300],
#     "Stock": [1000, 500, 800, 400, 600]
# }

# df = pd.DataFrame(data)

# average_price = df["Price"].mean()

# print("Average Price:", average_price)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# given a dataframe of students' scores in subjects , use loc ,and iloc to access specific rows and columns
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math": [90, 80, 70, 85],
    "Science": [85, 75, 95, 80],
    "English": [80, 70, 90, 75]
}

df = pd.DataFrame(data)

print(df.iloc[1:2, 1:2]) 

print(df.loc[["Bob", "Charlie"], ["Math", "English"]])

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!