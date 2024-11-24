
# ! counts the number of vowels (a, e, i, o, u) in the sentence.
count = 0
sentence=input("enter a sentence")
for char in sentence:
    if char.lower() in 'aeiou':
        count += 1

print(count)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! double each element in the list and store the result in a new list
list1=[1, 3, 5, 7, 9]
list2=[2*i for i in list1]
print(list2)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! Write a Python program to find the union and intersection of the two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)
print("the union is : ",union)
print("the intersection is : ",intersection)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! swap the keys and values in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {value: key for key, value in my_dict.items()}
print(swapped_dict)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! change the second element in a tuple to 12 () => [] => ().
tuple_before=(5, 10, 15, 20)
tuple_to_list=[*tuple_before]
tuple_to_list[1]=12
tuple_after=tuple(tuple_to_list)
print(tuple_after)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! is palindrome
text='asdfdsa'
def is_palindrome(text):
    for i in range(0, len(text)//2):
        if text[i] != text[len(text)-i-1]:
            return False
    return True 

print(is_palindrome(text))
# ! another solution
def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome(text))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! Input: [1, 2, 2, 3, 4, 2, 5], target = 2 >> doing something like this
# ! Output: {1: 1, 2: 3, 3: 1, 4: 1, 5: 1, 'target_count': 3}
l=input('enter a list').split()
t=input('enter a target')
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d,"target count is : ",d[t])
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! generate sequence of numbers starting from 1. Stop when the sum of all numbers in the list exceeds 200
l=[1]
while sum(l) < 200:
    l.append(l[-1]+1)
print(l)
print("Sum of all numbers is " + str(sum(l)))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! Remove daplicated data from a list
l=[1, 2, 2, 3, 4, 4, 5]
print(list(set(l)))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! dict from unique words in the list, and the values are lists containing the indices (positions)
input_list = ["apple", "banana", "orange", "banana", "kiwi", "apple"]
words_to_indices ={}

for index, word in enumerate(input_list):
    if word not in words_to_indices:
        words_to_indices[word] = [index]
    else:
        words_to_indices[word].append(index)

print(words_to_indices)