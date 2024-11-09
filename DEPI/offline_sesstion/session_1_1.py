# Files
path="D:/AI/Python_Projects/first_project_python/DEPI/offline_sesstion/"
# ! get data from user and print it line by line
def getUserData():
    try:
        first_name=input("Enter your first name : ")
        last_name=input("Enter your last name : ")
        gender=input("Enter your gender : ")
        id=int(input("Enter your Id : "))
    except:
        print("an error happened")    
    else:
        with open(f"{path}session_1.txt","w") as file:
            file.write(first_name+"\n")
            file.write(last_name+"\n")
            file.write(gender+"\n")
            id=str(id)
            file.write(id+"\n")
getUserData()
with open(f"{path}session_1.txt",'r') as file:
    for line in file:
        print(line.strip())