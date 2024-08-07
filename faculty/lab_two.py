print("*"*50)
# ! Excercise 1
# Loops from -5 to 5
# for num in range(-5,5):
#     print(num)
# ! Excercise 2 
# playList=[10,9.5,4,2,5,2,10,8,7.5,29,34]
# for num in playList:
#     if (num>6):
#         print(num)
#     else:
#         break
# ! Excercise 3
# colors=["purplr","red","green","orange","yellow","pink"]
# newColors=[]
# for color in colors: 
#     if(color != "orange"):
#         newColors.append(color)
#     else:
#         break
# print(newColors)
# ! Excercise 4
# word="ABCDEFG"
# print(word[0:3])
# print(word[::2])
#! Excercise 5
dic={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
    }
word="one two two three three three four four four four five five five five five"
for value in dic.values():
    print(f"number {value} repeted : { word.count(value)} times")