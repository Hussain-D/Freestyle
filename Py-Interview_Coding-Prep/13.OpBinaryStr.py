"""
Question 2: 

(Asked in Accenture OnCampus 10 Aug 2022, Slot 2)

Problem Description :
The Binary number system only uses two digits, 0 and 1 and 
number system can be called binary string. 
You are required to implement the following function:

int OperationsBinaryString(char* str);

The function accepts a string str as its argument. 
The string str consists of binary digits separated with an alphabet as follows:

    - A denotes AND operation
    - B denotes OR operation
    - C denotes XOR Operation

You are required to calculate the result of the string str, 
scanning the string to right taking one opearation at a time, 
and return the same.

Note:

    No order of priorities of operations is required
    Length of str is odd
    If str is NULL or None (in case of Python), return -1

Input:
str: 1C0C1C1A0B1

Output:
1

Explanation:
The alphabets in str when expanded becomes “1 XOR 0 XOR 1 XOR 1 AND 0 OR 1”, 
result of the expression becomes 1, hence 1 is returned.

Sample Input:
0C1A1B1C1C1B0A0

Output:
0
"""
"""Longer approach with Recursion"""
# def OperationBinaryString(st):
#     res = int(st[0])
    
#     if st[1]=='A':
#         res = res & int(st[2])
#         if len(st)==3:
#             st = str(res)
#             return st
#         st = str(res) + st[3:]
#         print("st =",st)
#     elif st[1]=='B':
#         res = res | int(st[2])
#         if len(st)==3:
#             st = str(res)
#             return st
#         st = str(res) + st[3:]
#         print("st =",st)
#     if st[1]=='C':
#         res = res ^ int(st[2])
#         if len(st)==3:
#             st = str(res)
#             return st
#         st = str(res) + st[3:]
#         print("st =",st)
#     return OperationBinaryString(st)

# st = input("str: ")
# print(-1 if st=="" else OperationBinaryString(st))

"""Shorter Approach"""
def OperationBinaryString(st):
    res = int(st[0])
    i = 1
    while len(st)<i:
        if st[1]=='A':
            res &= int(st[2])
        elif st[1]=='B':
            res |= int(st[2])
        else:
            res ^= int(st[2])
        i += 2
    return res

st = input("str: ")
print(-1 if st=="" else OperationBinaryString(st))