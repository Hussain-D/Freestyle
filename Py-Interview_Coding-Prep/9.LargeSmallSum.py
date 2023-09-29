"""
def LargeSmallSum(arr)

The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.

Assumption

    Every array element is unique.
    Array is 0 indexed.

Note:

    If the array is empty, return 0.
    If array length is 3 or <3, return 0.
     

Example

Input:
Arr: 3 2 1 7 5 4

Output:
7
 

Explanation

    The second largest element at the even position is 3.
    The second smallest element at the odd position is 4.
    The output is 7 (3 + 4).
"""

def LargeSmallSum(l):
    if len(l)==0 or len(l)<=3:
        return 0
    else:
        
        #finding second smallest at odd position
        odd_index = [l[i] for i in range(len(l)) if i%2!=0]
        odd_index.sort()
        sec_smal_odd = odd_index[0] if len(odd_index)<3 else odd_index[1]
        #finding second largest at even position
        even_index = [l[i] for i in range(len(l)) if i%2==0]
        even_index.sort()
        sec_lar_eve = even_index[0] if len(even_index)<3 else even_index[-2]
        
        return sec_smal_odd+sec_lar_eve
    
l = list(map(int,input().split())) 
print("Output:",LargeSmallSum(l))