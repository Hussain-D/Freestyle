""" 
    SLIDING WINDOW
    Input  : arr[] = {100, 200, 300, 400}, k = 2
    Output : 700

    Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4
    Output : 39
    We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

    Input  : arr[] = {2, 3}, k = 3
    Output : Invalid
    There is no subarray of size 3 as size of whole array is 2.

Naive Approach: So, let's analyze the problem with Brute Force Approach. 
We start with first index and sum till k-th element. 
We do it for all possible consecutive blocks or groups of k elements. 
This method requires nested for loop, 
the outer for loop starts with the starting element of the block of k elements and 
the inner or the nested loop will add up till the k-th element.

"""

arr_list = list(map(int,input("Enter the array: ").strip().split()))
k = int(input("Enter window size(k): "))
# print(arr_list,k)

if len(arr_list)<k:
    print("Invalid")
else:
    summax = 0
    for i in range(len(arr_list)-k+1):
        summ = 0
        for j in range(k):
            summ += arr_list[i+j]
            # print(summ,end="-")
        summax = max(summax,summ)
    print(summax)