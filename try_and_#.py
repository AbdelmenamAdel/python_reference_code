
# # ! quiz 1
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# #   ! quiz 2
# from math import PI
# def area_of_circle(radius):
#     return PI * radius**2
# radius = float(input("Enter the radius of the circle: "))
# area = area_of_circle(radius)
# print("The area of the circle is: ", area)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# #   ! quiz 3
# def primeORnot(num):
#     if num > 1:
#         for i in range(2, int(num ** 0.5) + 1):
#             if (num % i) == 0:
#                 return False
#         return True
#     else:
#         return False

# def prime_from_1_to_100():
#     primes = []
#     for i in range(1, 101):
#         if primeORnot(i):
#             primes.append(i)
#     return primes

# # Get the list of primes
# primes = prime_from_1_to_100()
# print(primes)

# # Create a dictionary with primes and their squares
# pc_dict = {i: i**2 for i in primes}
# print(pc_dict)
