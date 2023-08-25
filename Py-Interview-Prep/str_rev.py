"""
Q #1) How can you reverse a string?

Answer: String is reversed with the following algorithm:

    Initiate
    The string which is to be reversed is declared.
    Get the length of the string.
    Start a loop and then swap the position of the array elements.
    Keep the exchanged positions.
    Print the reversed string.

"""
strinp = input("Give me: ")

#Python way - list slicing
print(strinp[::-1])

#Basic way - pure logic
str_len = len(strinp)
rev_str = ""
for i in range(str_len,0,-1):
    rev_str += strinp[i-1]
print(rev_str)