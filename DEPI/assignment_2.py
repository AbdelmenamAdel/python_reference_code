
# ! Python Task 2 - Extract and Analyze List Slices
products = [
    ("Laptop", 1200, 5),
    ("Smartphone", 700, 10),
    ("Headphones", 150, 15),
    ("Monitor", 300, 7)
]
threshold = 500
products_above_threshold = []
for product in products:
    if product[1] > threshold:
        products_above_threshold.append(product[0])
print("Products above the price threshold:", products_above_threshold)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! Python Task 2 - Salary Increment
salaries = {
    101: 50000,
    102: 60000,
    103: 55000
}
increments = [
    (101, 10),  # 10% increment
    (104, 5),   # 5% increment, not in salaries
    (102, 15)
]

for id, increment in increments:
    if id in salaries:
        salaries[id] += (salaries[id] * increment) // 100 # double slash // is floor division

print(salaries)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! quiz 1 - FizzBuzz from 1 to 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   ! quiz 2 - Area of Circle
from math import PI
def area_of_circle(radius):
    return PI * radius**2
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print("The area of the circle is: ", area)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   ! quiz 3 - Create a dictionary with primes and their squares from 1 to 100
def primeORnot(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def prime_from_1_to_100():
    primes = []
    for i in range(1, 101):
        if primeORnot(i):
            primes.append(i)
    return primes

# Get the list of primes
primes = prime_from_1_to_100()
print(primes)

# Create a dictionary with primes and their squares
pc_dict = {i: i**2 for i in primes}
print(pc_dict)
