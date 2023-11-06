"""
Q #2) What is a palindrome string?
Answer: After the string is reversed as discussed in Q #1, we need to put the following condition:
Code snippet:

if(actualtxt.equals(reversetxt)){
   return “Palindrome”;
else
     return “Not Palindrome”;
}

Thus palindrome string is the one which on reversing remains the same, 
for example, - 'madam' is a palindrome string.
"""

"""
But first, What is palindrome? (string == gnirts --> palindrome)    
"""

# st = input("String: ").lower()

#print(True if st==st[::-1] else False)
#instead, a function can be made to return only \
#palindrome strings from a list of strings

def palin(s):
    return True if s==s[::-1] else False

listofstr = ['abc','aba','bbb','ryw','sam']

"""#--> 1 Naive approach"""
# palin_list_of_str = []
# for i in listofstr:
#     if palin(i):
#         palin_list_of_str.append(i)
# print(listofstr)
# print(palin_list_of_str)

"""#--> 2 list compre"""
# palin_list_of_str = []
# palin_list_of_str = [i for i in listofstr if palin(i)]
# print(listofstr)
# print(palin_list_of_str)

"""#--> 3 map & filter"""
# palin_list_of_str = []
# palin_list_of_str = list(filter(palin,listofstr))
# print(listofstr)
# print(palin_list_of_str)