from session_1_2 import Calculator 
cal = Calculator()

flag='y'
while flag=='y':
    x=int(input("Enter the first number : "))
    y=int(input("Enter the first number : "))
    operator =input("Enter the operator : ")
    try:
        if operator == '+':
            result = cal.add(x, y)
            print(f"{x} + {y} = {result}")
        elif operator == '-':
            result = cal.sub(x, y)
            print(f"{x} - {y} = {result}")
        elif operator == '*':
            result = cal.mul(x, y)
            print(f"{x} * {y} = {result}")
        elif operator == '/':
            if y != 0:
                result = cal.div(x, y)
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