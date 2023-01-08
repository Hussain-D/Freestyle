num1 = int(input())

# l = [[i for i in range(num1)] for j in range(num1)]

# print(l)

"""
print like this >
for input 5
    2
   3 5
  7 11 13
 17 19 23 29
8797 98797997
    
"""
def prime(num1):
    l_p = []
    for i in range(2,num1+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count==2:
            l_p.append(i)        
    return l_p

l_of_ps = prime(num1)

# for j in range(num1):
#     for i in range(num1-1):
#         print(" ",end='')
#     for i in range(j):
#         print(l_of_ps[:j+1],end=' ')
#         l_of_ps = l_of_ps[j+1:]
#     print('\n')

print(l_of_ps)

"""
The above problem is incomplete!!!
"""