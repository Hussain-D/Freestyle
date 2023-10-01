"""
def Productsmallpair(sum,arr)

This function accepts the integers sum and arr. It is used to find the arr(j) and arr(k), where k ! = j. arr(j) and arr(k) should be the smallest elements in the array and return the product of element of this pair.

Keep this in mind:

    If n<2 or empty, return -1.
    If these pairs are not found, then return to zero.
    Make sure all the values are within the integer range.
     

Example

Input:
Sum: 9
Arr: 5 4 2 3 9 1 7

Output:
2

Explanation

From the array of integers, we have to select the two smallest numbers, i.e 2 and 1. Sum of these two (2 + 1) = 3. This is less than 9 (3 < 9). The product of these two is 2 (2 x 1 = 2) Hence the output is integer 2.

Sample input:
Sum: 4
Arr: 9 8 -7 3 9 3

Sample output:
-21
"""

su = int(input("Sum: "))
arr = list(map(int,input("Arr: ").split()))

def Productsmallpair(su,arr):
    if len(arr)<2:
        return -1
    else:
        arr.sort()
        s1,s2 = arr[0],arr[1]
        return 0 if (s1+s2)>su else s1*s2
    
print("Output:",Productsmallpair(su,arr))