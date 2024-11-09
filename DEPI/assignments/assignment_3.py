
# ! Count Vowels in a String
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

text = input("Enter a text: ")
vowel_count = count_vowels(text)
print(f"The number of vowels in the text is: {vowel_count}")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Find the Maximum Value in a List Using a Function using file !!!!!
path="D:/AI/Python_Projects/first_project_python/DEPI/assignments/"
def find_max_value(numbers):
    if not numbers:
        return None
    max_value = int(numbers[0])
    for num in numbers:
        if int(num) > max_value:
            max_value = int(num)
    return max_value
def read_file_line_by_line():
    with open(f"{path}assignment_3.txt","r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

numbers = read_file_line_by_line()
max_value = find_max_value(numbers)
print("Maximum value:", max_value)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!! get user info and save it to a text  ﬁle. !!!!!!!!!!
path="D:/AI/Python_Projects/first_project_python/DEPI/assignments/"
def getUserData():
    try:
        first_name=input("Enter your first name : ")
        last_name=input("Enter your last name : ")
        gender=input("Enter your gender : ")
        id=int(input("Enter your Id : "))
    except:
        print("Oops, something went wrong, try again later...")    
    else:
        with open(f"{path}assignment_3.txt","w") as file:
            file.write("first name : "+first_name+"\n")
            file.write("last name : "+last_name+"\n")
            file.write("gender : "+gender+"\n")
            id=str(id)
            file.write("id : "+id+"\n")
getUserData()
with open(f"{path}assignment_3.txt",'r') as file:
    for line in file:
        print(line.strip())
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! simulate a calculator. Your funs are in a separate script calc.py
from assignment_3_calc import Calculator
calc = Calculator()

flag='y'
while flag=='y':
    x=int(input("Enter the first number : "))
    y=int(input("Enter the first number : "))
    operator =input("Enter the operator : ")
    try:
        if operator == '+':
            result = calc.add(x, y)
            print(f"{x} + {y} = {result}")
        elif operator == '-':
            result = calc.sub(x, y)
            print(f"{x} - {y} = {result}")
        elif operator == '*':
            result = calc.mul(x, y)
            print(f"{x} * {y} = {result}")
        elif operator == '/':
            if y != 0:
                result = calc.div(x, y)
                print(f"{x} / {y} = {result}")
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid operator. Please use +, -, *, /.")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input. Please enter integers only.")
    else:
        flag = input("Do you want to perform another operation? (y/n): ")