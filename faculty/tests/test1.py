
############## ! Abdelmoneim Adel Abdelmoneim ##############
################ ? Section 2 - AI Department ###############
# given an input string, count occurrences of all chars within a string

def count_occurrences(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

string = input("Enter a string: ")
print(count_occurrences(string))