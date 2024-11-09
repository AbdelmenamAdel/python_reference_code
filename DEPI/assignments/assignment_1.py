#!/usr/bin/env python
# coding: utf-8

# ## Python Task

# ### 1. Question: Merge and Sort Two Lists
# 
# **Description:** Given two lists of integers, merge them into one list and sort the result in ascending order. Do not use Python's built-in sort() function or other sorting functions.
# 
# 
# 

# In[ ]:


'''
# Example Input:
list1 = [3, 1, 4]
list2 = [2, 5, 0]

# Example Output:
[0, 1, 2, 3, 4, 5]'''


# In[ ]:





# ### 2. Question: Repeat Characters in a String
# 
# **Description:** Given a string, create a new string by repeating each character in the original string n times. 
# 
# Assume n is given and always a positive integer. 
# 
# Do not use if statements in your solution.
# 

# In[ ]:


'''
# Example Input:
s = "abc"
n = 3

# Example Output:
"aaabbbccc"

'''


# ## Write a program that accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers
# 

# - Enter a sequence of comma-separated numbers:  1,2,3,4
# - List: ['1', '2', '3', '4']
# -
# Tuple: ('1', '2', '3', '4')





# # !!!!!!!!!!!! Merge and Sort two lists !!!!!!!!!!!!
list1 = [3, 1, 4]
list2 = [2, 5, 0]
list3=list1+list2

for i in range(len(list3)):
    for j in range(len(list3)-1):
        if(list3[j]>list3[j+1]):
            temp=list3[j]
            list3[j]=list3[j+1]
            list3[j+1]=temp
print(list3)
# !!!!!!!!!!!! Repeat Characters in a string !!!!!!!!!!!!
x=input("Enter a string: ")
n=int(input("Enter number: "))
for i in range(len(x)):
    for j in range(n):
        print(x[i],end="")
# # !!!!!!!!!!!! Generates a list and a tuple from the comma separated numbers !!!!!!!!!!!!
x=input("Enter a sequence of comma-separated numbers: ")
list1=x.split(",")
tuple1=tuple(list1)
print("List: ",list1)
print("Tuple: ",tuple1)